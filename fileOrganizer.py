import os
import shutil

path=input("enter the directory you want sorted: ")
listOfFile=os.listdir(path)

for file in listOfFile:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
    