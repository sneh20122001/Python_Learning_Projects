from pytubefix import YouTube

# link = "https://youtu.be/h13RYohtLv0?si=AS6RPRaWaBKv3fDv"
# youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)
# videos = youtube_1.streams.all() # ALL FORMAT
# # videos = youtube_1.streams.filter(only_audio=True) # Only Audio
# vid = list(enumerate(videos))

# for i in vid:
#     print(i)

# print()
# strm = int(input("Enter : "))
# videos[strm].download()
# print("Successful")

from pytubefix import Playlist

py = Playlist("https://youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&si=-1jiUPMpecJAuxbk")
print(py.title)

for video in py.videos:
    video.streams.first().download()