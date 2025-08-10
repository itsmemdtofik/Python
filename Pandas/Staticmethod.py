# ! Static Method in Python


# Static methods are a type of method in Python that belong to a class rather than to an instance of the class.
# They are defined using the @staticmethod decorator and do not take the instance (self) or class (cls) as the first parameter.
# Static methods can be called on the class itself or on instances of the class, but they do not have access to instance-specific data or class-specific data.
# They are typically used for utility functions that are related to the class but do not require access to instance or class data.


# Here's an example to illustrate the use of static methods:    
class Dog:
    species = "Canine"  # class variable (common to all dogs)

    def __init__(self, name, age):
        self.name = name  # object variable
        self.age = age

    def bark(self):  # normal method (needs self / object)
        print(f"{self.name} says Woof!")

    @staticmethod
    def is_puppy(age):  # static method (no self, no cls)
        return age < 2


#
# Let's use the static method:
# create two dogs (objects)
dog1 = Dog("Buddy", 1)
dog2 = Dog("Rocky", 4)

# 1. Normal method (needs object)
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Rocky says Woof!

# 2. Static method (no object needed)
print(Dog.is_puppy(dog1.age))  # Output: True (because 1 year is a puppy)
