#import os to delete the file

import os
#os.remove("file handling/delete.txt")
#or

if os.path.exists("file handling/delete.txt"):
    os.remove("file handling/delete.txt")
else:
    print("file not found")

#to delete empty folder
os.rmdir("file handling/deletefold")
