thistuple = ("Apple", "Banana","Mango")

print(thistuple)

#As tuple are indexed
print(thistuple[0])

#As tuple are unchangeable - meaning that we can not change, add or remove items after the tuple has been created.
#thistuple[0] = "Orange"
print(thistuple)

#print(thistuple.remove("Apple"))

#print(thistuple.append("Pineapple"))

#* Tuple can store different data types as list
tuple1 = ("apple", "banana", "cherry", 23)
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)


#** It is also possible to create the tuple using the constructor.
mytuple = tuple(("banana","mango","orange"))
print(mytuple)

#!But there is a solution that if we want to change the tuple then first convert it into the list then we can modify this.

x = ("apple","mango","orange","cherry")
y = list(x)

y[0] = "SanDisk"
x = tuple(y)

print(x)

#! We can unpack the tuple using asterisk(*)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print("Green : ", green)
print("Yellow", yellow)
print("Red", red)

#!We can join the tuple
#!We can unpack the tuple


