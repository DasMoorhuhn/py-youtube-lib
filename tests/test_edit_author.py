from unittest import TestCase

from src.helper import edit_author


class TestEditAuthor(TestCase):
  yt_music_account = 'Currents - Topic'
  yt_account = 'Currents'

  def test_edit_author(self):
    author = edit_author(self.yt_account)
    self.assertEqual(author, self.yt_account)

    author = edit_author(self.yt_music_account)
    self.assertEqual(author, self.yt_account)
