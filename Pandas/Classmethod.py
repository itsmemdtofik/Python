"""
# ! Class method in Python:
# Class method is a built-in decorator in Python that is used to define a method that belongs to the class rather than an instance of the class.
#When you define a method with the @classmethod decorator, the first parameter of that method is always the class itself (usually named cls), not an instance of the class (which is usually named self).
# This allows you to call the method on the class itself, rather than on an instance of the class.
# The main use case for class methods is to create factory methods that can create instances of the class using different sets of parameters.
# Class methods can also be used to access or modify class-level attributes.
"""


# Here's an example to illustrate the use of class methods:
class Dog:
    species = "Canine"  # class variable (common to all dogs)

    def __init__(self, name, age):
        self.name = name  # object variable
        self.age = age

    def bark(self):  # normal method (needs self / object)
        print(f"{self.name} says Woof!")

    @classmethod
    def change_species(cls, new_species):  # class method (needs cls)
        cls.species = new_species

    @staticmethod
    def is_puppy(age):  # static method (no self, no cls)
        return age < 2


# Let's use all of them:

# create two dogs (objects)
dog1 = Dog("Buddy", 1)
dog2 = Dog("Rocky", 4)

# 1. Normal method (needs object)
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Rocky says Woof!

# 2. Static method (no object needed)
print(Dog.is_puppy(dog1.age))  # Output: True (because 1 year is a puppy)
print(Dog.is_puppy(dog2.age))  # Output: False

# 3. Class method (change something for whole class)
Dog.change_species("WolfDog")
print(Dog.species)  # Output: WolfDog
print(dog1.species)  # Output: WolfDog
print(dog2.species)  # Output: WolfDog

# In this example:
# Class methods are useful when you want to define methods that are related to the class itself rather than to instances of the class.
# They can be used for factory methods, class-level operations, and more.
# In summary, class methods are a powerful feature in Python that allows you to define methods that operate on the class itself rather than on instances of the class.
# They are defined using the @classmethod decorator and take the class as the first parameter (usually named cls).
# This allows you to create factory methods, access class-level attributes, and perform class-level operations.
