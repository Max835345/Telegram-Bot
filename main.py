import moviepy.editor
import os
from pathlib import Path
from pytube import YouTube


link = input()
name = input()
yt = YouTube(link)
streams = yt.streams
vd = streams.filter(progressive=True).desc().first().download(filename=f"{name}.mp4")
video_file = Path(f'{name}.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file}.mp3')
os.rename(f'{name}.mp4.mp3',f'{name}.mp3')
