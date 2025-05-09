
#! Metaclass In Python

'''
* Metaclasses are classes of classes. They define how classes behave and are created. 
* While regular classes create objects, metaclasses create classes. 
* By using metaclasses, you can modify class definitions, enforce rules, or add functionality during class creation
'''

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct) #This calls the parent (type) to actually create the class using normal mechanisms.
    
class MyClass(metaclass=Meta):
    pass

#Output: Creating class MyClass
'''
Meta is a custom metaclass, and it inherits from type.

type is the built-in Python metaclass that normally creates classes.

__new__ is a special method that controls the creation of instances — here, it controls the creation of classes.

🔵 The parameters to __new__:

cls: the metaclass itself (Meta).

name: name of the class being created (MyClass here).

bases: a tuple of parent classes (() because MyClass doesn’t inherit anything).

dct: dictionary containing attributes of the class (functions, variables)

'''

#! Another method to creat Metaclass in python
class Meta(type):
    def __init__(cls, name, bases, dct):
        print(f"Class {name} initialized")
        super().__init__(name, bases, dct)

class MyClass(metaclass=Meta):
    pass

'''
Another approach is to override the __init__ method of a metaclass rather than __new__. 
While __new__ creates the class, __init__ is called after the class is created, so it’s used for initialization.
'''