try:
    from pytubefix import YouTube
except ModuleNotFoundError:
    print('請先進入終端機 輸入以下\npip install --upgrade pytube')
    exit()
import os
import ssl
import tkinter as tk
from tkinter import messagebox
ssl._create_default_https_context = ssl._create_stdlib_context  # ssl驗證

win = tk.Tk()   # GUI視窗
src_y = win.winfo_screenheight()
src_x = win.winfo_screenwidth()
size = f'400x200+{(src_x-400)//4}+{(src_y-200)//4}'  # 視窗大小
win.geometry(size)
win.resizable(False,False)
win.configure(bg="#b6dbb7")
win.title("YT to MP3 (Python)")
win.tk.call('wm', 'iconphoto', win._w, tk.PhotoImage(file='icon.png'))  # icon設定

def change():
    global option
    try:
        option.destroy() # 刪除選單
        option_list.clear() # 選單 資料清除
        yt_list.clear()  # YT 檔案清除
        option_w.set("請選擇")  # 選單 文字
        
        url = word.get()  # YT連結
        yt = YouTube(url)  # YT物件
        music = yt.streams.filter(only_audio=True,subtype='mp4').order_by('abr') # 音樂檔
        video = yt.streams.filter(file_extension='mp4',progressive=True) # 影片檔
        
        yt_list.extend(music)
        yt_list.extend(video)
        for i in music:
            option_list.append(f'音檔：{i.abr}')
        for j in video:
            option_list.append(f'影片：{j.resolution}({j.fps}fps)')
        notice.set("請選擇 並按「下載」")
        option = tk.OptionMenu(win,option_w,*option_list)  # 選單 設定
        option.config(bg="#b6dbb7",width=14)  # 選單-樣式
        option.place(x=85,y=75) # 選單 顯示
        bt_download.place(x=255,y=74)  # 下載鈕 顯示
    except:
        notice.set("此影片無法下載 非常抱歉\n請嘗試在終端機輸入「pip install --upgrade pytube」\n或更改連結！")

def download():
    t = option_list.index(option_w.get())
    target_path = ""
    
    out_file = yt_list[t].download(output_path=target_path)
    base, ext = os.path.splitext(out_file)
    if option_list[t].count("音檔")>0:   # 如果是音檔
        new_file = base + ' Music.mp3'
    else:
        new_file = base + ' Movie.mp4'
    os.rename(out_file, new_file)
    notice.set(f'「{option_list[t]}」下載完成\n\n下載位置：{new_file}')
    print(f"target path = {new_file}\nFile has been successfully downloaded.") # cmd回報狀況

t = tk.Label(win,text="YouTube to MP3",
             font=("微軟正黑體",20,"bold"),
             bg="#b6dbb7").pack()
word = tk.Entry(win,bd=2,width=35,fg="gray")
word.pack(pady=3,padx=7,anchor='nw')

def on_entry_click(*s):
    if word.get() == "請輸入YT連結":
        word.delete(0, "end")  # 刪除文字
        word.config(fg="black")  # 將字體改成黑色

word.insert(0, "請輸入YT連結")  # 設置提示
word.bind("<FocusIn>", on_entry_click)  # 當輸入欄取得焦點 執行on_entry_click

bt_change = tk.Button(win,
               text="轉換",
               activeforeground="green",
               command=change,
               padx=3,pady=3).place(x=345,y=39)
bt_download = tk.Button(win,
               text="下載",
               activeforeground="red",
               command=download,
               padx=3,pady=3)
bt_download.place(x=105,y=74)
bt_download.place_forget()
option_w = tk.StringVar()
option_w.set("請選擇")
option_list = ["請選擇"]
yt_list = []
option = tk.OptionMenu(win,option_w,*option_list)

def no_choose(*s):
    if option_w.get()=="請選擇":
        bt_download.config(state='disabled')
    else:
        bt_download.config(state='normal')
option_w.trace('w',no_choose)  # 選單文字改變時 將下載鍵鎖定

notice = tk.StringVar()
end = tk.Label(win,textvariable=notice,
               bg="#b6dbb7",
               wraplength=350).pack(side="bottom",pady=3)

def question():
    messagebox.showinfo(parent=win,title="使用說明",
                        message="Step1：貼上YT連結\nStep2：按下 [轉換]\nStep3：選擇下載格式\nStep4：按下 [下載]")

img_q = tk.PhotoImage(file="question.png").subsample(2,2)
bt_question = tk.Button(image=img_q,command=question).place(x=5,y=5)

win.mainloop()