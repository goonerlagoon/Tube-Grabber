import json
from yt_dlp import YoutubeDL
from pathlib import Path
# import tkinter as tk
from tkinter import filedialog as fd

# root = tk.Tk()
# root.title("Greetings Human")


# dict to load all process vars like 'dl_folder'
data = {}

try:
    with open('ydl_data.txt', 'r') as f:
        data = json.loads(f) # dump process vars into program
except FileNotFoundError:
    print("First time running the script? Let's get you set up then.")
    chosen_dir = fd.askdirectory(title="Select Default Download Destination")
    dl_fldr = Path(chosen_dir)
    data['dl_folder'] = dl_fldr.resolve()
    data['archive_file'] = (dl_fldr / 'ydl_archive.txt').touch(exist_ok=False)
    
    chosen_file = ''
    while chosen_file.endswith('.txt') != True:        
        chosen_file = fd.askopenfilename(title="Select Archive File. If it does"
                                        "not exist, choose a directory"
                                        "to make it in. Hit Cancel to"
                                        "choose the current working"
                                        "directory")
        if Path(chosen_file).is_file():
            if Path(chosen_file).suffix == '.txt':
                data['archive_file'] = chosen_file
                break
            else:
                continue
        else: #has to be a directory if not a file
                a_file = Path(chosen_file / 'archive_file.txt')
                a_file.touch(exist_ok=False)
                data['archive_file'] = a_file.resolve()
               
    
        
    dl_fldr = Path(data['dl_folder'] / 'ydl_data.txt')
    dl_fldr.touch(exist_ok=False)
    
except PermissionError:
    print("Insufficient permission to read that file")
    

    
url_to_download = "https://www.youtube.com/playlist?list=PLzfMfiJ36mokTWgmaZgOdq3utSSbEaAIf"

ydl_opts = { 
    'format': 'bestaudio',
    'cookiesfrombrowser': ('chrome', 'Profile 1'),
    'download_archive': f'{data["archive_file"]}',
    'postprocessors': [{  
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
        'outtmpl': f"{data['dl_folder'] + '%(title)s.%(ext)s'}"
        },  
        {
        'key': 'FFmpegMetadata',  
        }],
    
        }
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url_to_download])    



# archive_file = fd.askopenfilename(title="Select Archive File")
# proc_list = ['yt-dlp', '--cookies-from-browser', 'chrome:Profile 1', 
#              '-x', '--audio-format', 'mp3', '--abort-on-error', 
#              '--audio-quality', '0', playlist, '--download-archive', archive_file, '-o', dl_folder, '--exec',
#              'stdout=STDOUT', 'check=True', 'text=True']

# completed_proc = subprocess.run(proc_list)

# ydl_opts = {'format': 'bestaudio'}
# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    
# chosen_folder = ""
# try:
#      with open(dl_folder) as f:
#        chosen_folder = f.readline()
# except Exception as e:
#      print(e)
#      while (chosen_folder == "."):
#           chosen_folder = str(Path(filedialog.askdirectory(title="Select Download Destination")))
        
# root = tk.Tk()
# root.title("Greetings Human")
# while (chosen_folder == ""):
#      chosen_folder = str(Path(filedialog.askdirectory(title="Select Download Destination")))

# subprocess.run(["yt-dlp", ])

     
# print(chosen_folder)
# root.mainloop()
