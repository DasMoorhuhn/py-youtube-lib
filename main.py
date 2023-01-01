from classes import YtPlaylist, YtVideo

url = 'https://music.youtube.com/playlist?list=PLlypPVRGSnlsxaK7ZyRPTU_FNH3ctNdwo'

def men():
    print("")
    print("Type URL to the video or playlist")
    return input(">>> ")

def choice(url):
    if 'playlist?list=' in url:
        yt = YtPlaylist(url)
        yt.downloadAudio()
    else:
        yt = YtVideo(url)
        yt.download()

choice(men())