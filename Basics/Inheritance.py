
#! Inheirtance in Python
#* Inheritance gives the power to a class to access all attributes and method of another class.

class ParentClass:
    # Parent class attributes/methods
    pass

class ChildClass(ParentClass):  # Inherits from ParentClass
    # Child class can add/modify behavior
    pass


#! Lets take a real world example

#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some Sound!"
    

#Child Class(Inherit from Parent class)
class Dog(Animal):
    def speak(self):
        return "Woof!" #Method overriding (modifying the parent behavior)
    

#Usage
animal = Animal("Genric Animal")
print(animal.speak()) # Output: Some Sound!

dog = Dog("Buddy")
print(dog.name) #Output: Buddy (Inherited from Animal)
print(dog.speak()) #Output: "Woof!" (Overriden method)


#!Types of Inheritance

#! 1. Single Inheritance : 
# 1. A child class inherits from one parent class. 
# Example: Dog inherits from Animal.
class Animal:  # Parent class
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Child class
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Inherited from Animal → "Some sound"
print(dog.bark())   # Defined in Dog → "Woof!"

#! 2. Multiple Inheritance
#A child class inherits from multiple parent classes.
#Example: HybridCar inherits from ElectricEngine and PetrolEngine.
class ElectricEngine:
    def electric_power(self):
        return "Using electric power"

class PetrolEngine:
    def petrol_power(self):
        return "Using petrol power"

class HybridCar(ElectricEngine, PetrolEngine):  # Inherits from both
    def hybrid_mode(self):
        return "Both engines active"

car = HybridCar()
print(car.electric_power())  # From ElectricEngine
print(car.petrol_power())    # From PetrolEngine
print(car.hybrid_mode())     # From HybridCar


#! 3. Multilevel Inheritance
#A child class inherits from a parent, which itself inherits from another parent.
#Example: Puppy → Dog → Animal.
class Animal:
    def breathe(self):
        return "Breathing"

class Dog(Animal):  # Level 1 inheritance
    def bark(self):
        return "Woof!"

class Puppy(Dog):   # Level 2 inheritance
    def cry(self):
        return "Whimper..."

puppy = Puppy()
print(puppy.breathe())  # From Animal → "Breathing"
print(puppy.bark())     # From Dog → "Woof!"
print(puppy.cry())      # From Puppy → "Whimper..."


#! 4. Hierarchical Inheritance
#Multiple child classes inherit from one parent class.
#Example: Dog and Cat inherit from Animal.
class Animal:
    def eat(self):
        return "Eating food"

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.eat())  # Inherited from Animal → "Eating food"
print(cat.eat())  # Inherited from Animal → "Eating food"
print(dog.bark()) # Unique to Dog → "Woof!"
print(cat.meow()) # Unique to Cat → "Meow!"


#! 5. Hybrid Inheritance
#A combination of multiple and multilevel inheritance.
#Example: Student → Person (Single) + Person → Human (Multilevel) + Student → Scholar (Multiple).
class Human:
    def alive(self):
        return "I am human"

class Person(Human):  # Single inheritance
    def greet(self):
        return "Hello!"

class Scholar:
    def study(self):
        return "Studying hard"

class Student(Person, Scholar):  # Hybrid (Single + Multiple)
    def exam(self):
        return "Exam time!"

student = Student()
print(student.alive())  # From Human → "I am human"
print(student.greet())  # From Person → "Hello!"
print(student.study())  # From Scholar → "Studying hard"
print(student.exam())   # From Student → "Exam time!"
