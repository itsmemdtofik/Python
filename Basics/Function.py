#! Python Function


#!Printing the fisrt and last name

def name(fname, lname):
    print(f"First name:{fname} and last name:{lname}")

name("Mohammad", "tofik")

#! We can pass multiple argument(Arbitrary argument args*) into the function

def afunction(*kids):
    print(f"The yougest child is : {kids[1]}")

afunction("A", "B", "C")

#! Keyword argument
def myfunction(**kid):
    print("His last name is:", kid["lname"])

myfunction(fname = "A", lname = "B")

#! We can pass a list to an argument
def funclist(food):
    for x in food:
        print(x)

fruits = ["apple", "mango", "orange"]
funclist(fruits)