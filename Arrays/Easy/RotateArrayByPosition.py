# **************************
# Problem: Rotate Array by D Positions - Counter Clockwise or Left
# **************************

# Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

# Example 1:
# Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
# Output: {3, 4, 5, 6, 1, 2}
# Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

# Example 2:
# Input: arr[] = {1, 2, 3}, d = 4
# Output: {2, 3, 1}
# Explanation: The array is rotated as follows:
# After first left rotation, arr[] = {2, 3, 1}
# After second left rotation, arr[] = {3, 1, 2}
# After third left rotation, arr[] = {1, 2, 3}
# After fourth left rotation, arr[] = {2, 3, 1}

# **************************
# Python Solution:
# **************************

def rotate_array_in_counterclockwise(arr, d):
    """
    Simple solution: First store the first element of the array in a variable.
    Then, shift each element one by one and place them in the previous index.
    Repeat the process for `d` positions.
    This is a very basic solution.
    """
    
    # Handle the case where d >= len(arr), reducing d to d % len(arr)
    d = d % len(arr)
    
    first = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    
    arr[len(arr) - 1] = first
    
    second = arr[0]
    for j in range(len(arr) - 1):
        arr[j] = arr[j + 1]
    
    arr[len(arr) - 1] = second
    
    return arr

def reverse(arr, left, right):
    """
    Helper function to reverse the elements of the array between indices left and right.
    """
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_array_by_d_position(arr, d):
    """
    Method-2: Using a helper function.
    Step1: Rotate the entire array from 0 to arr.length - 1
    Step2: Rotate the first part from 0 to d - 1.
    Step3: Rotate the second part from d to arr.length - 1.
    """
    
    if len(arr) < 1:
        return arr
    
    # Handle the case where d >= len(arr), reducing d to d % len(arr)
    d = d % len(arr)
    
    # Step1: Reverse the entire array
    reverse(arr, 0, len(arr) - 1)
    
    # Step2: Reverse the first part (0 to d-1)
    reverse(arr, 0, d - 1)
    
    # Step3: Reverse the second part (d to len(arr)-1)
    reverse(arr, d, len(arr) - 1)
    
    return arr

# Example usage:

arr = [1, 2, 3, 4, 5, 6]
d = 2
print(f"Original Array: {arr}")
rotated_arr = rotate_array_by_d_position(arr, d)
print(f"Array after rotating by {d} positions counterclockwise: {rotated_arr}")
