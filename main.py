from classes import YtPlaylist, YtVideo, YtChannel

def men():
    print("")
    print("Type URL to the video or playlist")
    #return input(">>> ")
    return "https://music.youtube.com/channel/UCGNrk1jAXPUUlmdEuayU18A?feature=share"

def choice(url):
    yt = YtChannel(url=url)
    yt.test()
"""
    if 'playlist?list=' in url:
        yt = YtPlaylist(url, editTags=True)
        yt.downloadAudio()
        #yt.getInfos()
    else:
        yt = YtVideo(url)
        yt.download()
"""
choice(men())
