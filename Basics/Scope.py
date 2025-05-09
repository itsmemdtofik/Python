
#! Scope in Python

#A variable is only availab;e from inside the region it is created. This is called scope.

#! 1. Local Scope
#A varible is created inside a function is called local scope and can one be used inside the function.
def function():
    x = 200
    print(x)

function()

#! 2. Function inside function

def newfunction():
    x = 200
    def create_new_function():
        print(x)
    create_new_function()

newfunction()

#! 3. Global Scope

x = 400

def afunction():
    global x 
    x = 1000
    print(x)

afunction()
print(x)

from Module import greeting, multiply
greeting("Mohammad")

x = multiply(5, 6)
print(x)
