# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:38:39 2020

@author: Ishita
"""

from gtts import gTTS
import os
import shutil
home = os.getcwd()
#print(home)
mytext = input("Enter the text you want to hear: ")
language = "en"

myobj = gTTS(text=mytext, lang=language)
name = input("Enter the name of file: ")
name = name + ".mp3"
myobj.save(name)

try:
    os.makedirs(name.split(".")[0])
except OSError:
    print("Folder already exists.")
destination_folder = home + "\\" + name.split(".")[0]
#print(destination_folder)
source_folder = home + "\\" + name
#print(source_folder)
shutil.move(source_folder, destination_folder)
