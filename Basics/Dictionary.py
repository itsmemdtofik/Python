#! Python Dictionary also called hashtable or hashmap because it is key-value pair


details = {
    "name" : "Tofik",
    "company": "Sandisk",
    "Address" : "bengaluru",
    "age": 34,
    "Salary": 750000
}

#Updating or changing the dictionary using the update method and based on key
details['Address'] = "Mumbai"
details.update({"name":"Harun"})
print(details)

#! We can create using the dict() constructor

dictDetails = dict({"name" : "Tofik",
    "company": "Sandisk",
    "Address" : "bengaluru",
    "age": 34,
    "Salary": 750000})

print(dictDetails, type(dictDetails))

print("Printing the keys: ", dictDetails.keys(), type(dictDetails))
print("Printing the values ", dictDetails.values())
print("Using get() to access the value based on key ", dictDetails.get("name"))


#Print all the values in the dictionary, one by one
print("Print all the values in the dictionary, one by one")
for x in dictDetails:
    print(dictDetails[x])


#Print all the keys in the dictionary, one by one
print("Print all the keys in the dictionary, one by one")
for x in dictDetails:
    print(x)


#Print all the values in the dictionary, one by one
print("Print all the values in the dictionary, one by one")
for x in dictDetails.values():
    print(x)


#Print all the values in the dictionary, one by one
print("Print all the values in the dictionary, one by one")
for x in dictDetails.keys():
    print(x)

#Print all the items in the dictionary, one by one. One item is {'name': 'tofik'}
print("Print all the values in the dictionary, one by one")
for x, y in dictDetails.items():
    print(x, y)

#!Copying the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#! We can use dict() constructor to copy dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#! We can also have the nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#* Acees item in nested dictionary
print(myfamily["child2"]["name"])

#!Loop through nested dictionary
print("--------------------------------\n")
print("Loop through nested dictionary")
for x, y in myfamily.items():
    print("\n")
    print("Items",x)

    for z in y:
        print(z + ':', y[z])
        
