"""
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
"""
import numpy as np

numa = np.array(42)
numb = np.array([1, 2, 3, 4, 5])
numc = np.array([[1, 2, 3], [4, 5, 6]])
numd = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(numa.ndim)
print(numb.ndim)
print(numc.ndim)
print(numd.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(f"Number of dimension will be now 5: {arr}")

# Other way we can define the 2D

print_2D = np.array([(1, 2, 3, 4), (5, 6, 7, 8), (8, 9, 10, 11), (12, 13, 14, 15)])
print(f"This is another way to define the 2D arrays as you can see above: {print_2D}")
