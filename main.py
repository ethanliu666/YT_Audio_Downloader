import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from pytube import YouTube
import glob, os, shutil

status = ["Audio downloaded", "Download status pending", "Download failed"]

def download_music():
    vid_url = url.get()
    try:
        video = YouTube(vid_url)
        vid_audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        output_file = vid_audio.download()

        base, ext = os.path.splitext(output_file)
        new_file = base + ".mp3"
        os.rename(output_file, new_file)

        download_status.set(status[0])
        move_audio_files()

    except:
        download_status.set(status[2])


def move_audio_files():
    pattern = "\*.mp3"
    src_folder = r"C:\Users\ethan\PycharmProjects\music_downloader"
    dest_folder = r"C:\Users\ethan\Downloads"

    files = glob.glob(src_folder + pattern)

    for file in files:
        shutil.move(file, dest_folder)


root = Tk()
root.title("Youtube Audio Downloader")

mainframe = ttk.Frame(root, padding="80 80 100 100") # left top right bottom
mainframe.grid(column=0, row=0, sticky=NW)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

url = StringVar()
url_entry = tk.Entry(mainframe, width=50, textvariable=url)
url_entry.grid(column=2, row=1, sticky=E)

download_status = StringVar()
tk.Label(mainframe, textvariable=download_status, fg="#000000")\
    .grid(column=2, row=2, sticky=W)

tk.Button(mainframe, text="Download Audio", font=("Times New Roman", 10, "bold"),
          command=download_music, bg="#557a95", fg="#ffffff").grid(column=3, row=1, sticky=W)

tk.Label(mainframe, text="Enter URL",
         font=("Times New Roman", 11, "bold"), fg="#000000").grid(column=1, row=1, sticky=W)

tk.Label(mainframe, text="Status:",
         font=("Times New Roman", 11, "bold"), fg="#000000").grid(column=1, row=2, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=15, pady=15)


root.mainloop()