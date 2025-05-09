"""
* Maximum Consecutive One's or Zero in Binary Array.

Given a binary array, find the count of a maximum number of consecutive 1s
present in the array.

Examples:

Input: arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
Output: 4
Explanation: The maximum number of consecutive 1’s in the array is 4 from
index 8-11.

Input: arr = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
Output: 1
Explanation: The maximum number of consecutive 0’s in the array is 1 from
index 0-1.
"""

def maximum_consecutive(arr):
    """
    Function to find maximum consecutive 1's in the binary array.
    """
    if len(arr) == 0:
        return 0

    count_one = 0
    max_count = 0

    for num in arr:
        if num == 1:
            count_one += 1
            max_count = max(max_count, count_one)
        else:
            count_one = 0

    return max_count

def maximum_one_repeat(arr):
    """
    Another function to find maximum consecutive 1's in the binary array.
    (Same as maximum_consecutive with slightly different loop style)
    """
    count = 0
    result = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            result = max(result, count)
    return result

arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
print(f"Maximum consucutive of 1s is : {maximum_one_repeat(arr)}")