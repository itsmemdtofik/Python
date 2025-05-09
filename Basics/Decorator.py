
#! Decorator in Python


#** Decorator in python are essentially functions that add functionality to an existing function in Python without changeing
#** changing the structure of the function itself. They are represented as @decorator_name in Python and are called in bottom-up fashion.

def myDecorator(function):
    def wrapper():
        print("Something happened BEFORE function!")
        function()
        print("Something happened AFTER function!")
    return wrapper

@myDecorator
def sayHello():
    print("Hello, function()!")


sayHello()

#! Lets take decorator function to capitalize name

print("Lets take decorator function to capitalize name")

def name_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        return string_hello
    return wrapper

@name_decorator
def say_hello(name1, name2):
    return f"Hello {name1}! and Hello {name2}!"

say_hello("Digital", "SanDisk")