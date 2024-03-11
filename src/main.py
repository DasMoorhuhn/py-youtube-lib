import sys
sys.path.append('..')
from src.youtube_video import YtVideo
from src.youtube_playlist import YtPlaylist

from src.helper import use_list_file
from src.helper import link_is_video
from src.helper import link_is_yt_playlist
from src.helper import link_is_yt_music_playlist


def download_video(url: str):
  youtube = YtVideo(url=url)
  youtube.download()


def download_audio(url: str):
  youtube = YtVideo(url=url)
  youtube.download(as_audio=True)


def download_videos_from_playlist(url: str):
  youtube = YtPlaylist(url=url)
  youtube.download_video_files()


def download_audios_from_playlist(url: str):
  youtube = YtPlaylist(url=url)
  youtube.download_audio_files()


def download_from_list_file():
  links = use_list_file(file_name='')
  print(f"Downloading {len(links)} links from list")
  for link in links:
    if link_is_video(url=link): download_video(url=link)
    elif link_is_yt_playlist(url=link): download_videos_from_playlist(url=link)
    elif link_is_yt_music_playlist(url=link): download_audios_from_playlist(url=link)


