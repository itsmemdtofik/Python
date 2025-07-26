import math

"""
     * <pre>
     * ! Perfect Square : Binary Search:Time complexity: O(log(n)) Space complexity: O(1)
     * ! Math.Sqrt: Time complexity: O(1), Space complexity: O(1)
     * </pre>
"""


def usingBinarySearch(nums):
    """Check if a number is a perfect square using binary search."""
    if nums < 0:
        return False

    left, right = 0, nums
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == nums:
            return True
        elif square < nums:
            left = mid + 1
        else:
            right = mid - 1
    return False


def usingMathSqrt(nums):
    """Check if a number is a perfect square using math.sqrt()."""
    if nums < 0:
        return False
    sqrt = int(math.sqrt(nums))
    return sqrt * sqrt == nums


def countPerfectSquare(nums):
    """Count how many numbers in the array are perfect squares."""
    count = 0
    for i in nums:
        if usingBinarySearch(i):
            count += 1
    return count


arr = [4, 8, 16, 20, 25, 26]

for num in arr:
    if usingBinarySearch(num):
        print(f"{num} is a perfect square.")
    else:
        print(f"{num} is not a perfect square.")

print("The number of perfect squares in the array:", countPerfectSquare(arr))
