from pytube import YouTube
import os
from moviepy.editor import *
import time

url = input("url: ")
yt = YouTube(url)

yt.streams.get_lowest_resolution().download()

#https://www.youtube.com/watch?v=-tJYN-eG1zk

#
video = VideoFileClip(os.path.join(yt.title + ".mp4"))
video.audio.write_audiofile(os.path.join(yt.title + ".mp3"))
time.sleep(1)
video.close()
time.sleep(1)
os.remove(yt.title + ".mp4")
