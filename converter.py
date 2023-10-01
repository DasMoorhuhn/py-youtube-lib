from moviepy.audio.io.AudioFileClip import AudioFileClip


class Converter:
    def __init__(self) -> None:
        pass

    def MP4ToMP3(self, mp4, mp3):
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(mp3)
        FILETOCONVERT.close()
