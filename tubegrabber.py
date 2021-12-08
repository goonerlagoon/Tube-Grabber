import json
import os
import tkinter as tk
from pathlib import Path
from time import strftime  # used to create destination dir based on date
from tkinter import filedialog as fd

from yt_dlp import YoutubeDL

root = tk.Tk()
root.title("Greetings Human")
root.withdraw()


def seperator_sanitize(file_str: str) -> str:
    '''
    takes a file path as a string and returns the correct flavor
    of filepath seperator by casting to a Path object then recasting to
    string
    '''

    try:
        return str(Path(file_str))
    except TypeError:
        print("wrong type of object passed")


data = {}  # dict to load all vars like 'dl_folder' etc from json state file
data_file = 'ydl_data.json'

try:
    with open(data_file, 'r') as f:
        data = json.load(f)  # dump process vars into program
except FileNotFoundError:
    print("First time running the script it seems. Let's set up shop then.")
    chosen_dir = fd.askdirectory(title="Select Default Download Destination")
    data['dl_folder'] = seperator_sanitize(chosen_dir)

    data['url_to_download'] = input("Enter the playlist or video url")

    # make archive_text file to hold already dl'd vids
    archive_file = data['dl_folder'] + f'{os.sep}' + 'ydl_archive.txt'
    Path(archive_file).touch(exist_ok=False)
    data['archive_file'] = seperator_sanitize(archive_file)

    root.destroy()
    root.mainloop()

    # dumping downloader options into dict to be saved later
    data['ydl_opts'] = {
        'format': 'bestaudio',
        'cookiesfrombrowser': ('chrome', 'Profile 1'),
        'download_archive': data["archive_file"],
        # casting to Path object to get proper seperator, then recast to str
        # for JSON storage
        'outtmpl': seperator_sanitize(data["dl_folder"]) + f'{os.sep}' +
        strftime("%b-%d-%Y") + f'{os.sep}' + '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            },
            {
            'key': 'FFmpegMetadata',
            }],
        }

    try:
        with open(data_file, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)
    except Exception as e:
        print(f"JSON file didnt get dumped for some reason. \
              This is the err msg: {e}")

with YoutubeDL(data['ydl_opts']) as ydl:
    ydl.download([data['url_to_download']])

print("*" * 60)
print("All done!")
