def getSecondLargestNumber(nums: list[int]) -> int:
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None  # Handle case with no second largest


def getSecondLargestNumberII(arr: list[int]) -> int:
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


arr: list[int] = [1000, 2, 3, 10, 100, -100]

print(getSecondLargestNumberII(arr))
