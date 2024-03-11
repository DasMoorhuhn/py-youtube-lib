from pytube import YouTube
from pytube import Playlist
import progressbar
import os
import sys
import urllib.request
sys.path.append('..')

from src.helper import create_download_dir
from src.helper import edit_author
from src.helper import noop
from src.helper import string_album, string_single, string_songs
from src.edit_mp3 import edit_meta_tags
from src.convert_mp4_to_mp3 import mp4_to_mp3


class YtPlaylist:
  def __init__(self, url, edit_tags=False) -> None:
    self.yt = Playlist(url)
    self.videos = self.yt.videos
    self.count_videos = len(self.videos)
    self.saved_videos = []
    self.saved_mp3 = []
    self.artist = ""
    self.album = ""
    self.file_path = ""
    self.edit_tags = edit_tags

  def download_audio_files(self):
    pg_bar = progressbar.progressbar.ProgressBar(maxval=self.count_videos)
    count = 0
    folder_name = ""

    print(f"Download from {self.count_videos} files started...\n")
    print(self.yt.title)

    if self.yt.title == string_songs:
      first_song = self.videos[2]
      first_song: YouTube
      author = edit_author(first_song.author)
      folder_name = f"{author.strip()}"

    if self.yt.title == string_single: pass

    if string_album in self.yt.title:
      first_song = self.videos[0]
      first_song: YouTube
      author = edit_author(first_song.author)
      album_title = str(self.yt.title).split("Album - ")[1]
      self.artist = author
      self.album = album_title
      folder_name = f"{author.strip()}/{album_title.strip()}"

      path = f"Downloads/Playlists/{folder_name}"
      create_download_dir(path=path)

      icon_url = self.yt.sidebar_info[0][
        'playlistSidebarPrimaryInfoRenderer'][
        'thumbnailRenderer'][
        'playlistCustomThumbnailRenderer'][
        'thumbnail'][
        'thumbnails'][-1]['url']

      resource = urllib.request.urlopen(icon_url)
      output = open(f"Downloads/Playlists/{folder_name}/icon.png", "wb")
      output.write(resource.read())
      output.close()

    if folder_name == "": folder_name = self.yt.title

    pg_bar.start()
    for video in self.videos:
      video: YouTube
      pg_bar.update(count)
      path = f"Downloads/Playlists/{folder_name}"
      create_download_dir(path=path)
      self.saved_videos.append(video.streams.get_audio_only(subtype="mp4").download(output_path=path))
      count += 1
    pg_bar.finish()

    print("Download Done\n")
    print("Start convert files to MP3...\n")
    print(self.saved_videos)

    for file in self.saved_videos:
      file = str(file)
      file_path = file.split("/")
      file_name = file_path[-1]
      file_ending = file_name.split(".mp4")[0]
      file_path = file_path[:-1]
      final_file_path = ""

      for i in file_path: final_file_path += f"/{i}" if i != '' else noop()

      mp4_to_mp3(mp4_file=file, mp3_file=f"{str(final_file_path)}/{file_ending}.mp3")
      self.saved_mp3.append(f"{str(final_file_path)}/{file_ending}.mp3")
      self.file_path = final_file_path
      os.remove(path=file)
      print("\n")

    if self.edit_tags:
      print("\nEdit meta tags...\n")
      count = 1
      for file in self.saved_mp3:
        edit_meta_tags(mp3_file=file, artist=self.artist, album=self.album, track_nr=count, icon=f"{self.file_path}/icon.png")
        count += 1

  def download_video_files(self):
    count = 0
    pg_bar = progressbar.progressbar.ProgressBar(maxval=self.count_videos)
    pg_bar.start()

    for video in self.videos:
      video: YouTube
      pg_bar.update(count)
      path = f"Downloads/Playlists/{video.author}"
      create_download_dir(path=path)
      self.saved_videos.append(video.streams.get_highest_resolution().download(output_path=path))
      count += 1

    pg_bar.finish()
