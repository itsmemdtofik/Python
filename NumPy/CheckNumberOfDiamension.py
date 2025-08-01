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