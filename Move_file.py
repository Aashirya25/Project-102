import os
import shutil
source = "C:/Users/HP/Downloads"
destination = "C:/Users/HP/OneDrive - Nord Anglia Education/Pictures/Screenshots/Coding/Document_Files"

list_of_files = os.listdir(source)
print(list_of_files)

for file in list_of_files:
    root, extention = os.path.splitext(file)
    #print(root,ext)

    if extention == " ":
        continue
    if extention in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = source + '/' + file
        path2 = destination + '/' + "documentfiles"
        path3 = destination +'/' + "documentfiles" + '/' + file
        #print(path1)
        #print(path3)

        if os.path.exists(path2):
            print("Moving " + file + "...")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)
            print("Moving "+ file+"...")