from youtube_video import YtVideo
from youtube_playlist import YtPlaylist

from helper import use_list_file
from helper import link_is_yt_music_playlist
from helper import link_is_yt_playlist
from helper import link_is_video
from helper import noop


def download_video():
  youtube = YtVideo(url='')
  youtube.download()


def download_audio():
  youtube = YtVideo(url='')
  youtube.download(as_audio=True)


def download_videos_from_playlist():
  youtube = YtPlaylist(url='')
  youtube.download_video_files()


def download_audios_from_playlist():
  youtube = YtPlaylist(url='')
  youtube.download_audio_files()


def download_from_list_file():
  links = use_list_file(file_name='')


link_1 = 'https://www.youtube.com/watch?v=79Y6jfZ0wls'  # YT Video
link_2 = 'https://www.youtube.com/playlist?list=PLHrp_zHKy5pGAnDyQTtY8HT9nMhWq6nE1'  # YT Playlist
link_3 = 'https://music.youtube.com/playlist?list=OLAK5uy_m-bbsAaG0EbE6ATFt-cYlq8wNINT5VRA0'  # YTM Album


links = [link_1, link_2, link_3]
for link in links:
  print(link)
  print('YT Video') if link_is_video(url=link) else noop()
  print('YT Playlist') if link_is_yt_playlist(url=link) else noop()
  print('YTM Album') if link_is_yt_music_playlist(url=link) else noop()
  print('\n')
