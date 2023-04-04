#file detection
import os

path = "C:\\Users\\eL\\Desktop\\re.txt" # a path to a local file

if os.path.exists(path):
    print("That location exist")
    if os.path.isfile(path):
        print("That is a file ")
else:
    print("That location doesn't exist")