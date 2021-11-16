import subprocess
import datetime
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("Greetings Human")
chosen_folder = "."
while (chosen_folder == "."):
     chosen_folder = Path(filedialog.askdirectory(title="Select Download Destination"))

dl_folder = chosen_folder / 


# subprocess.run(["yt-dlp", ])

     
# print(chosen_folder)
# root.mainloop()
