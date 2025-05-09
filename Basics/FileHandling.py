
#! File handling in python

#! Reading from existing file
file = open("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt", "r")
print(file.read())

#!Writing to the file

with open("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt", "a") as f:
    f.write("I am working in Sandisk company.")


with open("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt", "r") as f:
    print(f.read())


with open("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt", "w") as f:
    f.write("Woops! I have deleted the contents.")

#!Overriting the existing content
with open("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt", "r") as f:
    print(f.read())


'''
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists
'''

#!Check if file exists
import os
if os.path.exists("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt"):
    os.remove("data.txt")
else:
    print("The file does not exists.")
#! To remove file
import os
os.remove("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt")

#To delete a folder use os.rmdir("foldername")