# importing packages
from pytube import YouTube
import os

# url input from user
yt = YouTube(
	str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
flag = True
while(flag):
    type = input("\nPress \"1\" for spotify download\nPress \"2\" to save in current directory\n>>")
    if(type == "1"):
         destination = "/Users/leonurny/Music/Spotify_Music/"
         flag = False
    elif(type == "2"):
        destination = "/Users/leonurny/Documents/Programmieren/Youtube_Downloader/"
        flag = False
    
# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
print("\ncurrent filename: " + base)
name = input("\nEnter file name:\n>>")
#new_file = name + '.mp3'
new_file = os.path.join(destination, name + '.mp3')

os.rename(out_file, new_file)

# result of success
print("\n---------------------------\nDownload successful\n--------------------------")