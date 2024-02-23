import os

# make sure that the file exists
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("the file does not exist")