from pathlib import Path

import os
def createFolder():
    name = input("enter folder name:")
    p = Path(name)
    p.mkdir()
    pass

def readFolder():
    p = Path("")
    items =list(p.rglob("*"))
    # for i in range(0,len(items)):
    for i ,v in enumerate(items):
        print(i+1,v)
    
def updating():
    readFolder()
    old_name = input("enter old name of your folder")
    old_path = Path(old_name)
    if old_path.exists:
        new_name = input("enter your new name of folder:")
        new_path = Path(new_name)
        old_path.rename(new_path)
        print("folder name renamed successfully")
    else:
        print("no such folder exists")

def deleteFolder():
    readFolder()
    name = input("enter folder name")
    p = Path("")
    if p.exists():
        p.rmdir()
        print(" Folder deleted")
    else:
        print(" Folder not exist")

# file crud
def createfile():
    readFolder()
    name = input("enter name of your file with extension: ")
    p = Path(name)
    if not p.exists():
        with open(name,"w") as fs:
            data = input("enter your data: ")
            fs.write(data)
            print("file created successfully")
    else:
        print("File already exists")

def readfile():
    readFolder()
    name = input("enter your file name to be read:")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(name, "r") as fs:
            print(fs.read())
    else:
        print("File does not exists ")


def deletefile():
    readFolder()
    name = input("enter file name to be deleted")
    p = Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print("file removed")
    else:
        print("file not exists")

def updatefile():
    name = input("enter your file name with extension:")
    p = Path(name)
    if p.exists() and p.is_file:
        print("print press 1 for updating file name")
        print("print press 2 for overwriting in file")
        print("print press 3 for appending  infile")
        choice = int(input("enter your choice:"))
        if choice ==1:
            new_name = input("new name for file:")
            new_path = Path(new_name)
            p.rename(new_path)
            print("file renamed successfully")
        if choice == 2:
            with open(name,"w") as fs:
                data = input("enter your data:")
                fs.write(data)
                print("data successfully overwrite.")
        if choice == 3:
            with open(name,"a") as fs:
                data = input("enter your data:")
                fs.write(" "+ data)
                print("data append in file.")

    else:
        print("not file exist")

def createfilefolder():
    readFolder()
    folder_name = input("enter your folder name:")
    file_name = input("enter your file name :")
    folder_path = Path(folder_name)
    file_path = folder_path/file_name
    if folder_path.exists() and folder_path.is_dir():
        if not file_path.exists():
            with open(file_path,"w") as fs:
                data = input("enter your data: ")
                fs.write(data)
                print("file created successfully")
        else:
            print("File already exists")
def deletefilefolder():
    readFolder()
    folder_name = input("enter your folder name:")
    file_name = input("enter your file name :")
    folder_path = Path(folder_name)
    file_path = folder_path/file_name
    if file_path.exists():
        os.remove(file_path)
        print("file removed succcessfully")
    else:
        print("invaild file name")
while True:

    print(" press 1 for creating folder:")
    print("press 2 for reading a folder:")
    print("press 3 for updating a folder:")
    print("press 4 for deleting a folder:")
    print("press 5 for creating a file:")
    print("press 6 for reading a file:")
    print ("press 7 for delete a file")
    print ("press 8 for update a file")
    print ("press 9 for creating file in specify folder")
    print ("press 10 for delete file in specify folder")

    print("press 0 for exit")
    check = int(input("enter your choice:"))
    if check == 1:
        createFolder()
    if check == 2:
        readFolder()
    if check == 3:
        updating()
    if check == 4:
        deleteFolder()
    if check == 5:
        createfile()
    if check == 6:
        readfile()
    if check == 7:
        deletefile()
    if check == 8:
        updatefile()
    if check == 9:
        createfilefolder()
    if check == 10:
        deletefilefolder()
    if check == 0:
        print("goodbye")
        break
    else:
        (" Invailds choice. choose between 0-10:")
