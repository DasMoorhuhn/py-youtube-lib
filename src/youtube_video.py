from pytube import YouTube

from helper import create_download_dir
from convert_mp4_to_mp3 import mp4_to_mp3


class YtVideo:
  def __init__(self, url) -> None:
    self.video = YouTube(url)

  def download(self, as_audio=False):
    print(self.video)
    print(self.video.title)
    path = f"Downloads/Videos/{self.video.author}"
    create_download_dir(path=path)
    self.video.streams.get_highest_resolution().download(output_path=path)
    if as_audio: mp4_to_mp3(mp4_file=f"{path}/{self.video.title}.mp4", mp3_file=f"{path}/{self.video.title}.mp3")
