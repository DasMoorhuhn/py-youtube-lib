import progressbar
import os
import urllib.request
import ytmusicapi

from pytube import YouTube
from pytube import Playlist
from mutagen.easyid3 import EasyID3
from eyed3.id3.frames import ImageFrame

from converter import Converter
from edit_mp3 import EditMP3


def createDownloadDir(path):
    try:os.makedirs(path)
    except: pass


class YtPlaylist:
    def __init__(self, url, editTags=False) -> None:
        self.yt = Playlist(url)
        self.ytMusicAPI = ytmusicapi.YTMusic(auth="oauth.json")
        self.videos = self.yt.videos
        self.countVideos = len(self.videos)
        self.savedVideos = []
        self.savedMP3 = []
        self.artist = ""
        self.album = ""
        self.year = self.ytMusicAPI.get_album(self.ytMusicAPI.get_album_browse_id(self.yt.playlist_id))['year']
        self.filePath = ""
        self.convert = Converter()
        self.editMP3 = EditMP3()
        self.editTags = editTags

    def __editAuthor(self, author:str):
        if "- Topic" in author:
            return author.split("- Topic")[0]
        
        if not "- Topic" in author:
            return author

    def downloadAudio(self):
        folder_name = ""
        print(f"Download from {self.countVideos} files started...\n")
        print(self.yt.title)

        if self.yt.title == 'Songs':
            first_song = self.videos[2]
            first_song:YouTube
            author = self.__editAuthor(first_song.author)
            folder_name = f"{author.strip()}"

        if self.yt.title == 'Single':
            pass

        if "Album - " in self.yt.title:
            first_song = self.videos[0]
            first_song:YouTube
            author = self.__editAuthor(first_song.author)
            albumTitle = str(self.yt.title).split("Album - ")[1]
            self.artist = author
            self.album = albumTitle
            folder_name = f"{author.strip()}/{albumTitle.strip()}"
            
            path = f"Downloads/Playlists/{folder_name}"
            createDownloadDir(path=path)

            iconURL = self.yt.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer']['thumbnailRenderer']['playlistCustomThumbnailRenderer']['thumbnail']['thumbnails'][-1]['url']
            resource = urllib.request.urlopen(iconURL)
            output = open(f"Downloads/Playlists/{folder_name}/icon.png","wb")
            output.write(resource.read())
            output.close()

        if folder_name == "":
            folder_name = self.yt.title

        pg_bar = progressbar.progressbar.ProgressBar(
            maxval=self.countVideos,
            term_width=60
        )
        pg_bar.start()
        count = 0

        for video in self.videos:
            video:YouTube
            pg_bar.update(int(count))
            path = f"Downloads/Playlists/{folder_name}"
            createDownloadDir(path=path)
            self.savedVideos.append(video.streams.get_audio_only(subtype="mp4").download(output_path=path))
            count += 1
        pg_bar.finish()

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
            print("\nEdit meta tags...\n")
            count = 1
            for file in self.savedMP3:
                self.editMP3.tags(mp3File=file, artist=self.artist, album=self.album, trackNR=count, date=self.year, icon=f"{self.filePath}/icon.png")
                count += 1

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


