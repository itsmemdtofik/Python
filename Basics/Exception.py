
#!Exception in Python


#! Divide by zero exception

try:
    num = int(input("Enter a number : "))
    print(10 / num)
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Can not divide by zero")

#! else and finally block
#else runs if no exception occurs
#finally always runs used for cleanup




#! Real world example

def readFile(filename):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "No read permission"

print(readFile("/Users/itsmemdtofik/Downloads/DSA-In-Python/Basics/data.txt"))