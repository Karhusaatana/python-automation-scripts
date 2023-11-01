"""
Author: Otso Rouhiainen

Folder filtering script.

Can be run to Downloads folder and filters files to their correct location. 
If file type is not found, the file is put into 'Other' folder.

"""

import os
import shutil
from pathlib import Path

cwd = os.getcwd()
DOWNLOADS = 'D:\Downloads'

all_files = os.listdir(DOWNLOADS)

for filename in os.listdir(DOWNLOADS):
    f = os.path.join(DOWNLOADS, filename)
    if os.path.isfile(f):
        if os.path.exists('D:\Downloads\Pictures') and f.endswith('png') or f.endswith('jpg') or f.endswith('PNG') or f.endswith('JPG'):
            shutil.move(f, 'D:\Downloads\Pictures')
            print("is picture")
        elif os.path.exists('D:\Downloads\TextFiles') and f.endswith('txt'):
            shutil.move(f, 'D:\Downloads\TextFiles')
            print("is text")
        elif os.path.exists('D:\Downloads\Videos') and f.endswith('.mp4'):
            shutil.move(f, 'D:\Downloads\Videos')
            print("is a video")
        elif os.path.exists('D:\Downloads\Sounds') and f.endswith('.m4a') or f.endswith('.mp3'):
            shutil.move(f, 'D:\Downloads\Sounds')
            print("is a sound file")
        elif os.path.exists('D:\Downloads\Decks') and f.endswith('.dek'):
            shutil.move(f, 'D:\Downloads\Decks')
            print("is a deck")
        elif os.path.exists('D:\Downloads\Installers') and f.endswith('.exe'):
            shutil.move(f, 'D:\Downloads\Installers')
            print("is an installer")
        elif os.path.exists('D:\Downloads\Sheets') and f.endswith('.csv') or f.endswith('.xlsx'):
            shutil.move(f, 'D:\Downloads\Sheets')
            print("is an excel file")
        elif os.path.exists('D:\Downloads\Documents') and f.endswith('.pdf') or f.endswith('.docx') or f.endswith('.PDF') or f.endswith('.odt') or f.endswith('.dotx'):
            shutil.move(f, 'D:\Downloads\Documents')
            print("is a document")
        elif os.path.exists('D:\Downloads\ZipFiles') and f.endswith('.zip') or f.endswith('.7z'):
            shutil.move(f, 'D:\Downloads\ZipFiles')
            print("is a zip file")
        elif os.path.exists('D:\Downloads\PowerPoints') and f.endswith('.pptx') or f.endswith('.ppt') or f.endswith('.pptm') :
            shutil.move(f, 'D:\Downloads\PowerPoints')
            print("is a powerpoint")
        elif os.path.exists('D:\Downloads\Code') and f.endswith('.java') or f.endswith('.cpp') or f.endswith('.pro') or f.endswith('.py') or f.endswith('.html'):
            shutil.move(f, 'D:\Downloads\Code')
            print("is a code file")
        else:
            shutil.move(f, 'D:\Downloads\Others')
            print("other file")