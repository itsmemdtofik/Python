#List in python

list1 = ["apple","Banana","Cherry"]

#1. Print using the for loop
for i in list1:
    print(i)


#2. Loop through the Index Numbers
list1 = ["Mango", "Orange","Pineapple"]

#Use the range() and len() functions to create suitable iterable
for i in range(len(list1)):
    print(list1[i])

#3. Print using while 
list2 = ["A", "B", "C"]
i = 0
while i < len(list2):
    print(list2[i])
    i += 1


#4. Looping using list comprehension
[print(x) for x in list1]

#List Comprehension

fruits = ["Apple", "Banana","Cherry","Kiwi","Mango"]
new_list = []
for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)

#We can do it one line as well

create_new_list = [x.upper() for x in fruits if "a" in x]
print("New List is {}".format(create_new_list))


#Sorting the list
create_new_list.sort(reverse=True) #Descending order by default it is in ascending order
print(create_new_list)

#Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Copy the list to another list
thislist = ["apple","banana",'mango']
mylist = thislist.copy()
print(mylist)

#Another method is to copyt the list is 
anotherlist = ["apple","banana","mango"]
myanotherlist = list(anotherlist)

print("Copying list using the in-built function {} to another list".format(myanotherlist))

#We can copy the list using the slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(print("Copying list using the slice operator {} to another list".format(mylist)))

thelist = ["apple","banana","mango"]
del thelist
print(thelist)