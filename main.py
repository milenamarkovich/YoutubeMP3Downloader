from __future__ import unicode_literals
import youtube_dl
import os

class Main:

    # Prompt user for URL and use this to gather video_info, such as what to name the file
    video_url = input("Please input the URL of the video you would like to convert: ")
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    filename = f"{video_info['title']}.mp3"

    # Ask user where they would like to save the local file - if no file inputted save to Desktop
    path_to_save = input(r"Please enter the folder where you would like to save your mp3 file: ")
    SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Desktop/' + path_to_save

    # Download the video and save to the desired folder in environment
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([video_info['webpage_url']])

    # Let user know they have successfully downloaded the video
    print("\n\nGreat! Your song has been downloaded - you can find it in your Spotify Library called 'Local Files'!")
    print("If you would like to add your song to a playlist, click on the 3 dots on the right hand side of your song title in the Local Files library.")

if __name__ == '__main__':
    cp = Main()