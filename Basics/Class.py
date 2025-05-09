
#!Python Classes and Object

'''
1. What is a Class?
A class is a blueprint that defines:

Attributes (data) → Variables that store data (e.g., name, age).

Methods (functions) → Actions the class can perform (e.g., greet(), calculate().
'''

class Dog:

    #Declaring class attributes (shared by all instances)
    species = "Canis familiaries!"

    #Constructor that are used to initialize the object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
    
'''
2. What is an Object?
An object is a specific instance of a class.

Each object has its own unique data (attributes).

Objects can use methods defined in the class.
'''

# Create two Dog objects
dog1 = Dog("Buddy", 3)  # Object 1
dog2 = Dog("Milo", 5)   # Object 2

# Access attributes
print(dog1.name)  # Output: "Buddy"
print(dog2.age)   # Output: 5

# Call methods
print(dog1.bark())  # Output: "Buddy says Woof!"
print(dog2.bark())  # Output: "Milo says Woof!"

# Class attribute (shared)
print(dog1.species)  # Output: "Canis familiaris"

#!Real world example

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

# Usage
account = BankAccount("Alice", 1000)
print(account.deposit(500))  # Deposited $500. New balance: $1500
print(account.withdraw(200)) # Withdrew $200. New balance: $1300

'''
1. self in Python Classes
What is self?
self refers to the current instance of the class (i.e., the object being created/used).

It is automatically passed when calling a method (you don’t pass it explicitly).

Why is self needed?
Helps Python distinguish between instance variables (unique to each object) and local variables.

Without self, methods wouldn’t know which object’s data to modify.
'''

#!Without self
class Dog:
    def set_name(name):  # ❌ Missing `self`
        name = name      # ❌ Confusion: Is this a local or instance variable?

dog = Dog()
dog.set_name("Buddy")    # ❌ Error: set_name() takes 1 arg but 2 were given

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#! Object can also contains method

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()