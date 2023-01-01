from pytube import YouTube
from pytube import Playlist
from pytube import Channel
from moviepy.editor import *
from mutagen.easyid3 import EasyID3
from eyed3.id3.frames import ImageFrame
import progressbar
import eyed3
import os
import urllib.request

def createDownloadDir(path):
    try:os.makedirs(path)
    except:pass

class YtPlaylist:
    def __init__(self, url, editTags=False) -> None:
        self.yt = Playlist(url)
        self.videos = self.yt.videos
        self.countVideos = len(self.videos)
        self.savedVideos = []
        self.savedMP3 = []
        self.artist = ""
        self.album = ""
        self.filePath = ""
        self.percent = pp()
        self.convert = Converter()
        self.editMP3 = EditMP3()
        self.editTags = editTags

    def __editAuthor(self, author:str):
        if "- Topic" in author:
            return author.split("- Topic")[0]
        
        if not "- Topic" in author:
            return author

    def downloadAudio(self):
        pgBar = progressbar.progressbar.ProgressBar().start()
        count = 0
        folderName = ""
        print(f"Download from {self.countVideos} files started...\n")
        print(self.yt.title)
        if self.yt.title == 'Songs':
            firstSong = self.videos[2]
            firstSong:YouTube
            author = self.__editAuthor(firstSong.author)
            folderName = f"{author.strip()}"

        if self.yt.title == 'Single':
            pass

        if "Album - " in self.yt.title:
            firstSong = self.videos[0]
            firstSong:YouTube
            author = self.__editAuthor(firstSong.author)
            albumTitle = str(self.yt.title).split("Album - ")[1]
            self.artist = author
            self.album = albumTitle
            folderName = f"{author.strip()}/{albumTitle.strip()}"
            
            path = f"Downloads/Playlists/{folderName}"
            createDownloadDir(path=path)

            iconURL = self.yt.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer']['thumbnailRenderer']['playlistCustomThumbnailRenderer']['thumbnail']['thumbnails'][-1]['url']
            resource = urllib.request.urlopen(iconURL)
            output = open(f"Downloads/Playlists/{folderName}/icon.png","wb")
            output.write(resource.read())
            output.close()

        if folderName == "":
            folderName = self.yt.title
        
        for video in self.videos:
            video:YouTube
            progress = self.percent.pro(G=self.countVideos, W=count)
            pgBar.update(int(progress))
            path = f"Downloads/Playlists/{folderName}"
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
            self.savedMP3.append(f"{str(finalFilePath)}/{fileEnding}.mp3")
            self.filePath = finalFilePath
            os.remove(path=file)
            print("\n")

        if self.editTags:
            for file in self.savedMP3:
                self.editMP3.tags(mp3File=file, artist=self.artist, album=self.album, icon=f"{self.filePath}/icon.png")

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

    def tags(self, mp3File, artist, album, icon):
        audiofile = eyed3.load(mp3File)
        if (audiofile.tag == None):
            audiofile.initTag()

        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(icon,'rb').read(), 'image/png')

        audiofile.tag.save()

        audio = EasyID3(mp3File)
        audio['artist'] = artist
        audio['album'] = album
        audio.save()
