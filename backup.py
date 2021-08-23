import os
import shutil

source=input("enter folder name: ")
destination=input("enter folder name: ")
source=source+"/"
destination=destination+"/"
listOfFiles=os.listdir(source)

for files in listOfFiles:
    shutil.copy((source+files),destination)