from classes import YtPlaylist, YtVideo

url = 'https://music.youtube.com/playlist?list=OLAK5uy_mqhQtFjgSbufD0R-DhsZHMXpaequ1HCPc&feature=share'

def men():
    print("")
    print("Type URL to the video or playlist")
    return input(">>> ")

def choice(url):
    if 'playlist?list=' in url:
        yt = YtPlaylist(url)
        yt.downloadAudio()
        print(yt.savedVideos)
    else:
        yt = YtVideo(url)
        yt.download()

try:
    while True:
        choice(men())
except:
    print("exit...")
    exit(0)