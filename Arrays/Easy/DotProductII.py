def dot_product_zip(nums, arr):
    if len(nums) != len(arr):
        print("Arrays must be the same length!")
        return None
    return sum(x * y for x, y in zip(nums, arr))

a = [1, 2, 3]
b = [4, 5, 6]
result = dot_product_zip(a, b)
if result is not None:
    print(f"The dot product is: {result}")


import numpy as np
def dot_product_numpy(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Arrays must be the same length!")
        return None
    return np.dot(arr1, arr2)

arr = [1, 2, 3]
values = [4, 5, 6]
result = dot_product_zip(arr, values)
if result is not None:
    print(f"The dot product is: {result}")