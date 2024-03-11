import os
import shutil
from unittest import TestCase

from src.main import download_audio
from src.main import download_video


class TestYoutubeVideo(TestCase):
  link = 'https://www.youtube.com/watch?v=MvsAesQ-4zA'

  @classmethod
  def tearDownClass(cls):
    shutil.rmtree('./Downloads/Videos/Chisss')

  def test_download_youtube_video(self):
    download_video(url=self.link)
    self.assertTrue(os.path.exists('./Downloads/Videos/Chisss'))
    self.assertTrue(os.path.isfile('./Downloads/Videos/Chisss/1_Second_Video.mp4'))

  def test_download_youtube_audio(self):
    download_audio(url=self.link)
    self.assertTrue(os.path.exists('./Downloads/Videos/Chisss'))
    self.assertTrue(os.path.isfile('./Downloads/Videos/Chisss/1_Second_Video.mp3'))



