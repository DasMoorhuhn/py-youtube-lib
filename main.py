from classes import YtPlaylist, YtVideo
import os

if not os.path.exists("./oauth.json"):
    print("Please get the oauth.json file using the 'ytmusicapi oauth' command")
    exit(1)


def men():
    print("")
    print("Type URL to the video or playlist")
    return input(">>> ")


def download_youtube_music_playlist(url):
    yt = YtPlaylist(url, edit_tags=True)
    yt.download_audio()


def download_youtube_playlist(url):
    print("Convert to MP3?")
    convert = False
    user_input = str(input("(y/n) >>> "))
    if user_input.lower() == 'y':
        convert = True
    else:
        pass

    yt = YtPlaylist(url)
    yt.download_videos(convert_to_mp3=convert)



def download_single_video(url):
    yt = YtVideo(url)
    yt.download()


def choose(url):
    if 'playlist?list=' in url:
        if 'playlist?list=OLA' in url:
            download_youtube_music_playlist(url)

        # yt playlist
        if 'playlist?list=PLG' in url:
            download_youtube_playlist(url)

    else:
        download_single_video(url)


choose(men())
