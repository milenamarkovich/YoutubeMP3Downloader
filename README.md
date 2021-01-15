# YoutubeMP3Downloader
As a fan of non-English music, I often find the Spotify database lacking in songs and artists. I decided to take matters into my own hands and created a script to convert youtube videos to MP3 files so that I can access them from my Spotify 'Local Files' Library and add them to my playlists. 

## Tools
* This script uses the [youtube-dl](https://github.com/ytdl-org/youtube-dl/) library to covert youtube URL's to MP3 files. 
* In order to extract audio from the youtube video, make sure you download [ffmpeg](https://ffmpeg.org/download.html)

## Setup
1. Open your command prompt and install the necessary dependancies:
   1. Install youtube-dl: 'pip install youtube-dl' and 'pip install requirements.txt'
   1. Install ffmpeg: 'pip install ffmpeg' *you can check that you have correctly installed ffmpeg by typing 'ffmpeg' into the command line*
   
1. Create or choose a local folder in your Desktop in which to save your files - you can enter this file into the script directly or respond to the user prompt

1. Log into your Spotify account and access your Settings -> Local Files and make sure the 'Save Local Files' is on.
   1. Select to 'Show songs from' the folder you have chosen for your MP3 files
   
1. Run the file - you can do this by typing 'python main.py' into the command prompt

## Note on Spotify Local Files
* The [Spotify API](https://developer.spotify.com/documentation/web-api/) does not currently support adding Local Files to your playlist - if you would like to add your MP3 files to a playlist you will have to do so manually by logging into your Spotify account Your Library -> Local Files, where you can find your files. To add a song to a playlist click on the 3 dots on the right-hand side of your desired song title, and add to a personal playlist!

## ToDo
* Create web-format for other users to access this tool
