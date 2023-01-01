from classes import YtPlaylist, YtVideo

url = 'https://music.youtube.com/playlist?list=PLlypPVRGSnlsxaK7ZyRPTU_FNH3ctNdwo'

def men():
    print("")
    print("Type URL to the video or playlist")
    return input(">>> ")

def choice(url):
    if 'playlist?list=' in url:
        yt = YtPlaylist(url, editTags=True)
        yt.downloadAudio()
        #yt.getInfos()
    else:
        yt = YtVideo(url)
        yt.download()

try:
    while True:
        choice(men())
except:
    print("exit...")
    exit(0)