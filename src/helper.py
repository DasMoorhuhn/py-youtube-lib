import os

string_album = 'Album - '
string_topic = '- Topic'
string_single = 'Single'
string_songs = 'Songs'


def noop():
  """Do a no-op"""
  return lambda *a, **k: None


def create_download_dir(path: str) -> None:
  os.makedirs(name=path, exist_ok=True)


def edit_author(author: str):
  return author.split(string_topic)[0].strip() if string_topic in author else author


def use_list_file(file_name: str):
  with open(file_name, 'r') as file: return file.readlines()


def link_is_video(url: str) -> bool:
  return True if 'watch?v=' in url else False


def link_is_yt_music_playlist(url: str) -> bool:
  return True if 'playlist?list=OLA' in url else False


def link_is_yt_playlist(url: str) -> bool:
  return True if 'playlist?list=PL' in url else False


def replace_spaces(path: str):
  os.rename(src=path, dst=path.replace(' ', '_'))

