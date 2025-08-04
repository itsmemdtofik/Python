def getArrayByRotateRight(arr, k):
    if not arr:  # Handle empty array case
        return arr

    n = len(arr)
    k = k % n  # Normalize k to be within array bounds
    result = [0] * n  # Initialize result array

    for i in range(n):
        result[(i + k) % n] = arr[i]

    return result


print(getArrayByRotateRight([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(getArrayByRotateRight([1, 2, 3], 5))  # [2, 3, 1] (5%3=2)
print(getArrayByRotateRight([], 3))  # [] (edge case)
print(getArrayByRotateRight([1], 100))  # [1] (single element)
