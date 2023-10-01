from classes import YtPlaylist, YtVideo


def men():
    print("")
    print("Type URL to the video or playlist")
    return input(">>> ")


def choice(url):
    if 'playlist?list=' in url:
        print("Playlist")
        yt = YtPlaylist(url, editTags=True)
        yt.downloadAudio()
        # yt.getInfos()
    else:
        yt = YtVideo(url)
        yt.download()


choice(men())
