from pytube import YouTube

link = input("paste video Link here: ")
print("Start Downloading... ")
print(link)

yt = YouTube(link)

display_resolution = yt.streams.get_highest_resolution().resolution
print(display_resolution)

yt.streams.get_highest_resolution().download()
print("Video Downloaded Successfully. ")