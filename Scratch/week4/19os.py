import os

filelist = os.listdir(".")

for file in filelist:
    print(file)
print()

#dirs = os.walk(".")
#print("current folder, folders in folder, files:")
#for items in dirs:
#    print(items)
