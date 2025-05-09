#!Python Set

myset = {"apple", "mango", "Snadisk"}

#print(myset[0])
print("Mysets is : ", myset)

#! Set is unordered, immutable and do not allow duplicate
#! But you can remove item and add new item using add() method

#* We can join the two sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#!Join Sets
#There are several ways to join two or more sets in Python.

#The union() and update() methods joins all items from both sets.

#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

#The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

#set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

#!Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)