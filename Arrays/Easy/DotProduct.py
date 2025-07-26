"""
     * !Dot Product of two Array
     * !Approach: Time complexity: O(n), Space complexity: O(1)
     * Step1: Traverse the array
     * Step2: Multiply of both array and store the result
     * Step3: Return the result
"""

def DotProduct(nums, arr):

    dot_product = 0
    if len(nums) != len(arr):
        raise ValueError("Array must be the same length")
    else:
        i = 0
        while i < len(nums):
            dot_product += nums[i] * arr[i]
            i += 1
    return dot_product

number = [1, 2, 3]
values = [4, 5, 6, 5]

try:
    print(f"Dot Product: {DotProduct(number, values)}")
except ValueError as e:
    print(f"Error: {e}")
