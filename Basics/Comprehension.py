
#! Comprehension of List, Tuple, Dictionary in Python

#* 1. List
new_list = [i for i in range(1, 10)]
print("\n")
print("List Comprehension")
print(new_list)
print(new_list[::-1])

#* 2. Dictionary
print("\n")
print("Dictionary Comprehension")
new_dict = {i : i ** 2 for i in range(1, 10)}
print(new_dict)

#* 3. Tuple
print("\n")
print("Tuple Comprehension")
new_tuple = (i for i in range(1, 10))
print(new_tuple)

another_tuple = tuple(i for i in range(1, 10))
print(another_tuple)