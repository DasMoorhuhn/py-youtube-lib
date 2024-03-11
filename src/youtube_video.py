import sys
sys.path.append('..')
from pytube import YouTube

from src.helper import create_download_dir
from src.helper import replace_spaces
from src.convert_mp4_to_mp3 import mp4_to_mp3


class YtVideo:
  def __init__(self, url) -> None:
    self.video = YouTube(url)

  def download(self, as_audio=False):
    video_title = self.video.title.replace(' ', '_')
    print(self.video)
    print(self.video.title)
    path = f"Downloads/Videos/{self.video.author}"
    create_download_dir(path=path)
    self.video.streams.get_highest_resolution().download(output_path=path)
    replace_spaces(f"{path}/{self.video.title}.mp4")
    if as_audio: mp4_to_mp3(mp4_file=f"{path}/{video_title}.mp4", mp3_file=f"{path}/{video_title}.mp3")
