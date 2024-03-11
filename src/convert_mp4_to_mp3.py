from moviepy.editor import AudioFileClip


def mp4_to_mp3(mp4_file, mp3_file):
  """Converts mp4 file to mp3"""
  file_to_convert = AudioFileClip(mp4_file)
  file_to_convert.write_audiofile(mp3_file)
  file_to_convert.close()

