"""
Slicing arrays:

Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
"""
import numpy as np
nums = np.array([1, 2, 3, 4, 5, 6, 7])

print(nums[1:5])
print(nums[:4])
print(nums[4:])
print(nums[:4])


# Negative Slicing is also in python
print(f"Negative Indexing: ")
print(nums[-3:-1])
print(nums[::2])

#Slicing 2D-Array
print(f"Slicing 2D Array: ")
twoDNums = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(twoDNums[1, 1:4])

# From both elements return the index 2:
print(twoDNums[0:2, 2])

# From both elements, slice index 1 to 4 (not included), this will return 2:D arrays
print(twoDNums[0:2, 1:4])