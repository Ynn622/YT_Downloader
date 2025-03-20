from pytubefix import YouTube
import os
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context  # ssl驗證

# url=YT連結  target=目的位置
url = "https://www.youtube.com/watch?v=09NRL8MfoyI"
target_path = "/Users/BlackXD/Downloads"

yt = YouTube(url)  # 建立YT物件
print(yt.streams.filter(only_audio=True,subtype='mp4'))
music = yt.streams.filter(only_audio=True,subtype='mp4').order_by('abr')
musiclist = []
for i in music:
    musiclist.append(i.abr)
print(musiclist)
c = int(input("choose index:"))
out_file = music[c].download(output_path=target_path)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print("target path = " + (new_file))
print("mp3 has been successfully downloaded.")