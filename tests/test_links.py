from unittest import TestCase

from src.helper import link_is_yt_playlist
from src.helper import link_is_yt_music_playlist
from src.helper import link_is_video


class TestLinks(TestCase):
  link_yt_playlist = 'https://www.youtube.com/playlist?list=PLHrp_zHKy5pGAnDyQTtY8HT9nMhWq6nE1'
  link_yt_music_playlist = 'https://music.youtube.com/playlist?list=OLAK5uy_m-bbsAaG0EbE6ATFt-cYlq8wNINT5VRA0'
  link_yt_video = 'https://www.youtube.com/watch?v=79Y6jfZ0wls'
  link_yt_video_via_share_button = 'https://youtu.be/1ypgPv7cAPo?si=QWew2Y5PUwmrcNaF'

  def test_link_is_yt_playlist(self):
    link = link_is_yt_playlist(url=self.link_yt_playlist)
    self.assertTrue(link)

    link = link_is_yt_playlist(url=self.link_yt_music_playlist)
    self.assertFalse(link)

    link = link_is_yt_playlist(url=self.link_yt_video)
    self.assertFalse(link)

    link = link_is_yt_playlist(url=self.link_yt_video_via_share_button)
    self.assertFalse(link)

  def test_link_is_yt_music_playlist(self):
    link = link_is_yt_music_playlist(url=self.link_yt_playlist)
    self.assertFalse(link)

    link = link_is_yt_music_playlist(url=self.link_yt_music_playlist)
    self.assertTrue(link)

    link = link_is_yt_music_playlist(url=self.link_yt_video)
    self.assertFalse(link)

    link = link_is_yt_music_playlist(url=self.link_yt_video_via_share_button)
    self.assertFalse(link)

  def test_link_is_yt_video(self):
    link = link_is_video(url=self.link_yt_playlist)
    self.assertFalse(link)

    link = link_is_video(url=self.link_yt_music_playlist)
    self.assertFalse(link)

    link = link_is_video(url=self.link_yt_video)
    self.assertTrue(link)

    # link = link_is_video(url=self.link_yt_video_via_share_button)
    # self.assertTrue(link)





