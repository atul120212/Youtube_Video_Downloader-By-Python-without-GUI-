from pytube import YouTube
link = input("Enter Your YouTube Link : ")
youtube_1= YouTube(link)
print(youtube_1.title)
#print(youtube_1.thumbnail_url)
#audio = youtube_1.streams.filter(only_audio=True)
video = youtube_1.streams.all()
vid = list(enumerate(video))
for i in vid:
    print(i)
strm = int(input("Enter stream :"))
video[strm].download()
#audio[strm].download()
print("Download started!")