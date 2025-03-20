from pytubefix import YouTube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context  # ssl驗證

# url=YT連結  target=目的位置
url = "https://www.youtube.com/watch?v=JtxxpqbApn4"
target_path = "/Users/BlackXD/Downloads"

yt = YouTube(url, "WEB")  # 建立YT物件
video = yt.streams.filter(file_extension='mp4',progressive=True)
videolist = []
for i in video:
    videolist.append(f'{i.resolution}({i.fps}fps)')
print(videolist)
c = int(input("choose index:"))

out_file = video[c].download(output_path=target_path)
print(f"target path = {out_file}\nmp4 has been successfully downloaded.")