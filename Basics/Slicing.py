my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Positive Indexing

# Get elements from index 2 to 5 (5 not included)
print(my_list[2:5])  # Output: [2, 3, 4]

# Get every second element from index 1 to 7
print(my_list[1:7:2])  # Output: [1, 3, 5]


#Negative Indexing

# Get last three elements
print(my_list[-3:])  # Output: [7, 8, 9]

# Get elements from -5 to -2
print(my_list[-5:-2])  # Output: [5, 6, 7]

#Omitting Indices

# First 5 elements
print(my_list[:5])  # Output: [0, 1, 2, 3, 4]

# Everything from index 5 onward
print(my_list[5:])  # Output: [5, 6, 7, 8, 9]

# The entire list
print(my_list[:])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Step Parameter

# Every second element
print(my_list[::2])  # Output: [0, 2, 4, 6, 8]

# Reverse the list
print(my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Every third element, starting from index 1
print(my_list[1::3])  # Output: [1, 4, 7]