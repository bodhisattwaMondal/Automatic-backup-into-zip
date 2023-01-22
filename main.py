import os 
from zipfile import ZipFile

# Getting the Script Name in order to exclude it into the Backup zip file 
Script_dir = __file__.split("/")
Position = len(Script_dir)-1

# Listing all the contents of the current directory :
folder = os.listdir()
# Excluding the Script file :
# folder.remove(Script_dir[Position])

folderName = ""  # It will contain all the folder names present in the current directory
myList = []      # It will contain all the inner contents of the folders.

# Geting the Folder names :
for item in folder:
    folderName = str(item)
    # Appendig all the inner contents of the folder into a list :  
    for root, dirs, files in os.walk(folderName):
        for name in files:
            fileapath = os.path.join(root, name)
            myList.append(fileapath)

# Writing into zip file :
with ZipFile("Backup.zip",'w') as zip: 
        # Writing each file one by one 
        for file in myList: 
            zip.write(file) 

print("Succesfully zipped up !!")

# ©Bodhisattwa Mondal