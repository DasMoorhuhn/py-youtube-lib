from pytube import YouTube
from pytube import Playlist
from pytube import Channel
from moviepy.editor import *
import eyed3
import progressbar
import os

def createDownloadDir(path):
    try:os.makedirs(path)
    except:pass

class YtPlaylist:
    def __init__(self, url) -> None:
        self.yt = Playlist(url)
        self.videos = self.yt.videos
        self.countVideos = len(self.videos)
        self.savedVideos = []
        self.percent = pp()
        self.convert = Converter()

    def downloadAudio(self):
        pgBar = progressbar.progressbar.ProgressBar().start()
        count = 0
        print(f"Download from {self.countVideos} files started...\n")
        
        for video in self.videos:
            video:YouTube
            progress = self.percent.pro(G=self.countVideos, W=count)
            pgBar.update(int(progress))
            path = f"Downloads/Playlists/{str(self.yt.title).replace(' ', '_')}"
            createDownloadDir(path=path)
            self.savedVideos.append(video.streams.get_audio_only(subtype="mp4").download(output_path=path))
            count += 1
        pgBar.finish()

        print("Download Done\n")
        print("Start convert files to MP3...\n")

        for file in self.savedVideos:
            file = str(file)
            filePath = file.split("/")
            fileName = filePath[-1]
            fileEnding = fileName.split(".mp4")[0]
            filePath = filePath[:-1]
            finalFilePath = ""
            for i in filePath:
                if i == '':continue
                finalFilePath += f"/{i}"

            self.convert.MP4ToMP3(mp4=file, mp3=f"{str(finalFilePath)}/{fileEnding}.mp3")
            os.remove(path=file)
            print("\n")

    def downloadVideo(self):
        for video in self.videos:
            video:YouTube
            print(f"Started download: {video.title}")
            path = f"Downloads/Playlists/{video.author}"
            createDownloadDir(path=path)
            self.savedVideos.append(video.streams.get_highest_resolution().download(output_path=path))
            print("done\n")


class YtVideo:
    def __init__(self, url) -> None:
        self.video = YouTube(url)

    def download(self):
        print(self.video)
        print(self.video.title)
        path = f"Downloads/Videos/{self.video.author}"
        createDownloadDir(path=path)
        self.video.streams.get_highest_resolution().download(output_path=path)


class pp:
    def pro(self, G, W):
        if G == 0 and W == 0:
            return 100
        p = W/G
        p = round(p, 2)

        if p < 1:
            p = str(p).split(".")
            if p[1] == "1":
                return("10")
            elif p[1] == "2":
                return("20")
            elif p[1] == "3":
                return("30")
            elif p[1] == "4":
                return("40")
            elif p[1] == "5":
                return("50")
            elif p[1] == "6":
                return("60")
            elif p[1] == "7":
                return("70")
            elif p[1] == "8":
                return("80")
            elif p[1] == "9":
                return("90")
            else:
                return(str(p[1]))
        else:
            p = str(p).split(".")
            return("100")

class Converter:
    def __init__(self) -> None:
        pass

    def MP4ToMP3(self, mp4, mp3):
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(mp3)
        FILETOCONVERT.close()

class EditMP3:
    def __init__(self) -> None:
        pass

    def test(self, mp3File):
        pass
