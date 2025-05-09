
#! Polymorphism in Python

#! class polymorphism

print("class polymorphism")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Driver")
    


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Ford", "Mustag") #Create a car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object


for x in (car1, boat1, plane1):
    x.move()

#** Note: Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.

#!Inheritance class Polymorphism
#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
print("\n")
print("Inheritance class Polymorphism")

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  
  x.move()