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
    def __init__(self, url, edit_tags=False) -> None:
        self.yt = Playlist(url)
        self.yt_music_api = ytmusicapi.YTMusic(auth="oauth.json")
        self.videos = self.yt.videos
        self.count_videos = len(self.videos)
        self.saved_videos = []
        self.saved_mp3 = []
        self.artist = ""
        self.album = ""
        try:self.year = self.yt_music_api.get_album(self.yt_music_api.get_album_browse_id(self.yt.playlist_id))['year']
        except:pass
        self.file_path = ""
        self.convert = Converter()
        self.editMP3 = EditMP3()
        self.editTags = edit_tags

    def __edit_author(self, author:str):
        if "- Topic" in author:
            return author.split("- Topic")[0]
        
        if not "- Topic" in author:
            return author

    def __convert_to_mp3(self):
        # print("Convert to MP3...")
        # pg_bar = progressbar.progressbar.ProgressBar(
        #     maxval=self.count_videos,
        #     term_width=60
        # )
        # pg_bar.start()
        # count = 0

        for file in self.saved_videos:
            # pg_bar.update(count)
            file = str(file)
            file_path = file.split("/")
            file_name = file_path[-1]
            file_ending = file_name.split(".mp4")[0]
            file_path = file_path[:-1]
            final_file_path = ""
            for i in file_path:
                if i == '':continue
                final_file_path += f"/{i}"
            self.convert.mp4_to_mp3(mp4=file, mp3=f"{str(final_file_path)}/{file_ending}.mp3")
            self.saved_mp3.append(f"{str(final_file_path)}/{file_ending}.mp3")
            self.file_path = final_file_path
            os.remove(path=file)
            # count += 1
        # pg_bar.finish()

    def download_audio(self):
        folder_name = ""
        print(f"Download from {self.count_videos} files started...\n")
        print(self.yt.title)

        if self.yt.title == 'Songs':
            first_song = self.videos[2]
            first_song:YouTube
            author = self.__edit_author(first_song.author)
            folder_name = f"{author.strip()}"

        if self.yt.title == 'Single':
            pass

        if "Album - " in self.yt.title:
            first_song = self.videos[0]
            first_song:YouTube
            author = self.__edit_author(first_song.author)
            album_title = str(self.yt.title).split("Album - ")[1]
            self.artist = author
            self.album = album_title
            folder_name = f"{author.strip()}/{album_title.strip()}"
            
            path = f"Downloads/Playlists/{folder_name}"
            createDownloadDir(path=path)

            icon_url = self.yt.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer']['thumbnailRenderer']['playlistCustomThumbnailRenderer']['thumbnail']['thumbnails'][-1]['url']
            resource = urllib.request.urlopen(icon_url)
            output = open(f"Downloads/Playlists/{folder_name}/icon.png","wb")
            output.write(resource.read())
            output.close()

        if folder_name == "":
            folder_name = self.yt.title

        pg_bar = progressbar.progressbar.ProgressBar(
            maxval=self.count_videos,
            term_width=60
        )
        pg_bar.start()
        count = 0

        for video in self.videos:
            video:YouTube
            pg_bar.update(int(count))
            path = f"Downloads/Playlists/{folder_name}"
            createDownloadDir(path=path)
            self.saved_videos.append(video.streams.get_audio_only(subtype="mp4").download(output_path=path))
            count += 1
        pg_bar.finish()

        print("Download Done\n")
        print("Start convert files to MP3...\n")
        
        self.__convert_to_mp3()

        if self.editTags:
            print("\nEdit meta tags...\n")
            count = 1
            for file in self.saved_mp3:
                self.editMP3.tags(mp3File=file, artist=self.artist, album=self.album, trackNR=count, date=self.year, icon=f"{self.file_path}/icon.png")
                count += 1

    def download_videos(self, convert_to_mp3=False):
        print(f"Download from {self.count_videos} files started...\n")

        pg_bar = progressbar.progressbar.ProgressBar(
            maxval=self.count_videos,
            term_width=60
        )
        pg_bar.start()
        count = 0

        for video in self.videos:
            video:YouTube
            path = f"Downloads/Playlists/{video.author}"
            createDownloadDir(path=path)
            self.saved_videos.append(video.streams.get_highest_resolution().download(output_path=path))
            pg_bar.update(int(count))
            count += 1
        pg_bar.finish()
        print("done\n")

        if convert_to_mp3:
            self.__convert_to_mp3()


class YtVideo:
    def __init__(self, url) -> None:
        self.video = YouTube(url, use_oauth=True)

    def download(self):
        print(self.video)
        print(self.video.title)
        path = f"Downloads/Videos/{self.video.author}"
        createDownloadDir(path=path)
        self.video.streams.get_highest_resolution().download(output_path=path)


