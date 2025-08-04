def getMissingNumber(nums: list[int], number: int) -> int:
    return (number * (number + 1) // 2) - sum(nums)


def getMissingNumberII(arr, n):
    total = n * (n + 1) // 2
    for num in arr:
        total -= num
    return total


# 6. Find Missing Number
nums = [1, 2, 4, 5, 6]  # Missing 3
print("\nMissing Number:")
print(getMissingNumberII(nums, 6))  # 3
