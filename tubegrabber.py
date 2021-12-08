import json
from yt_dlp import YoutubeDL
from pathlib import Path
import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.title("Greetings Human")
root.withdraw()

def sep_sanitize(file_str):
    try:
        return str(Path(file_str))
    except TypeError:
        print("wrong type of object passed)
    

# dict to load all vars like 'dl_folder' etc from json state file 
data = {}
data_file = 'ydl_data.json'
  
data['url_to_download'] = "https://www.youtube.com/playlist?list=PLzfMfiJ36mokTWgmaZgOdq3utSSbEaAIf"

try:
    with open(data_file, 'r') as f:
        data = json.load(f) # dump process vars into program
except FileNotFoundError:
    print("First time running the script it seems. Let's set up shop then.")
    # casting resulting file string to Path object to get proper seperator
    chosen_dir = Path(fd.askdirectory(title="Select Default Download Destination")) 
    
    data['dl_folder'] = str(chosen_dir)
except PermissionError:
    print("Insufficient permission to read that file")

root.destroy()
root.mainloop()

# make archive_text file to hold already dl'd vids
archive_file = (Path(data['dl_folder']) / 'ydl_archive.txt')
archive_file.touch()
data['archive_file'] = str(archive_file)

data['ydl_opts'] = { 
    'format': 'bestaudio',
    'cookiesfrombrowser': ('chrome', 'Profile 1'),
    'download_archive': data["archive_file"],
    # casting to Path object to get proper seperator, then recast to str for
    # JSON storage
    'outtmpl': str(Path(data["dl_folder"])) + '\\' + '%(title)s.%(ext)s',
    'postprocessors': [{  
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
        },  
        {
        'key': 'FFmpegMetadata',  
        }],
    
    }

with YoutubeDL(data['ydl_opts']) as ydl:
    ydl.download([data['url_to_download']])
    
with open(data_file, 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)
    
print("All done!")