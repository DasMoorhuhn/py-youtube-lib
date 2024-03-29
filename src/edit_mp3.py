from mutagen.easyid3 import EasyID3
from eyed3.id3.frames import ImageFrame
import eyed3
import sys
sys.path.append('..')

from src.helper import noop


def edit_meta_tags(mp3_file, artist, album, track_nr, icon):
  audiofile = eyed3.load(mp3_file)
  audiofile.initTag() if audiofile.tag is None else noop()
  audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(icon, 'rb').read(), 'image/png')
  audiofile.tag.save()

  audio = EasyID3(mp3_file)
  audio['artist'] = artist
  audio['album'] = album
  audio['tracknumber'] = str(track_nr)
  audio.save()

  # Not deeded but nice to know
  """
  from mutagen.id3 import ID3NoHeaderError
  from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK
  
  # Read the ID3 tag or create one if not present
  try: 
      tags = ID3(fname)
  except ID3NoHeaderError:
      print("Adding ID3 header")
      tags = ID3()
  
  tags["TIT2"] = TIT2(encoding=3, text=title)
  tags["TALB"] = TALB(encoding=3, text=u'mutagen Album Name')
  tags["TPE2"] = TPE2(encoding=3, text=u'mutagen Band')
  tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'mutagen comment')
  tags["TPE1"] = TPE1(encoding=3, text=u'mutagen Artist')
  tags["TCOM"] = TCOM(encoding=3, text=u'mutagen Composer')
  tags["TCON"] = TCON(encoding=3, text=u'mutagen Genre')
  tags["TDRC"] = TDRC(encoding=3, text=u'2010')
  tags["TRCK"] = TRCK(encoding=3, text=u'track_number')
  
  tags.save(fname)
  """
