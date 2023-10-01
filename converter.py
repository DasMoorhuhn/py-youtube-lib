from moviepy.audio.io.AudioFileClip import AudioFileClip


class Converter:
    def __init__(self) -> None:
        pass

    def mp4_to_mp3(self, mp4, mp3):
        file_to_convert = AudioFileClip(mp4)
        file_to_convert.write_audiofile(mp3)
        file_to_convert.close()
