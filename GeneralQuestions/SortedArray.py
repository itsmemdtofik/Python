def getSortedArray(nums: list[int], ascending=True) -> bool:
    direction = 1 if ascending else -1
    return all(nums[i] * direction <= nums[i + 1] * direction for i in range(len(nums) - 1))


def getSortedArrayII(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


# 4. Sorted Array Check
sorted_arr = [1, 2, 3, 4, 5]
unsorted_arr = [3, 1, 4, 2, 5]
print("\nSorted Check:")
print(getSortedArrayII(sorted_arr))  # True
print(getSortedArray(unsorted_arr))  # False
