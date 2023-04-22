import numpy as np
import os
blacklist_txt = "C:\\Users\\Pablo\\Downloads\\photos_remove.txt"  #blacklist .txt file
parent_folder = "C:\\Users\\Pablo\\Desktop\\230421 - goofy TU Delft LinkedIn ahh photos"
blacklist = []

#open file and get the img names into a list
with open(blacklist_txt,"r") as f:
    for line in f:
        line = line.replace("\n","").split("-")
        line = [int(x) for x in line]
        if len(line) > 1:
            line = [x for x in range(line[0], line[1])]
        print(line)
        for photo in line:
            blacklist.append("_MG_"+str(photo))

print(blacklist)


for folders in os.listdir(parent_folder+"\\raw"):
    for f in blacklist:
        os.remove(os.path.join(parent_folder, "raw",folders,f"{f}{folders}"))    
        # for f in blacklist:
            
        # print(files)
        # os.remove()