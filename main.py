from classes import YtPlaylist, YtVideo


def men():
    print("")
    print("Type URL to the video or playlist")
    return input(">>> ")


def choice(url):
    if 'playlist?list=' in url:
        yt = YtPlaylist(url, editTags=True)
        yt.downloadAudio()
    else:
        yt = YtVideo(url)
        yt.download()


try:
    while True:choice(men())
except:
    exit(0)
