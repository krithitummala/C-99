import os
import shutil
source = input("Enter source folder name")
dest = input("Enter destination folder name")
print(source)
source1 = source+"/"
print(source1)
dest1 = dest+"/"
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source1+file),dest1)
