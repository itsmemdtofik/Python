# Numpy array indexing is same as we in the array or the list in the python

import numpy as np

nums = np.array([1, 2, 3, 4])

# Get the first element and the second element and add them using numpy
print(f"Adding the first:{nums[0]} and second element {nums[1]}: {nums[0] + nums[1]}")

# To access of 2D array we use comma seperated integers representing the dimension and the index of the element

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Access the element on the first row, second column
print(f"2nd element on 1st row: {arr[0, 1]}")

# Access the element on the 2nd row, 5th column
print(f"2nd element on 1st row: {arr[1, 4]}")

# To access of 2D array we use comma seperated integers representing the dimension and the index of the element
nums = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Access the third element of the second array of the first array
print(f"Third element of the second array of the first array: {nums[0, 1, 2]}")

print(f"First Matrix: {nums[0]}")
print(f"Second Matrix: {nums[1]}")

print(f"First Matrix of first row: {nums[0, 0]} ")
print(f"First Matrix of second row: {nums[0, 1]} ")
print(f"First Matrix ka first element: {nums[0, 0, 0]} ")

print(f"Second Matrix of first row: {nums[1, 0]} ")
print(f"Second Matrix of second row: {nums[1, 1]} ")

print(f"Second Matrix ka first element: {nums[1, 0, 0]} ")