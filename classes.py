from pytube import YouTube
from pytube import Playlist

import os

def createDownloadDir(path):
    try:os.makedirs(path)
    except:pass

class YtPlaylist:
    def __init__(self, url) -> None:
        self.yt = Playlist(url)
        self.videos = self.yt.videos
        self.savedVideos = []

    def downloadAudio(self):
        for video in self.videos:
            video:YouTube
            print(f"Started download: {video.title}")
            path = f"Downloads/Playlists/{video.author}"
            createDownloadDir(path=path)
            self.savedVideos.append(video.streams.get_audio_only(subtype="mp4").download(output_path=path))
            print("done\n")

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
        