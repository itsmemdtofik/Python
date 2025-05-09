# **************************
# Problem: Reverse an Array in Groups of Given Size
# **************************

# Given an array arr[] and an integer K, the task is to reverse every subarray formed by consecutive K elements.

# Example 1:
# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], K = 3 
# Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]

# Example 2:
# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], K = 5 
# Output: [5, 4, 3, 2, 1, 8, 7, 6]

# Example 3:
# Input: arr[] = [1, 2, 3, 4, 5, 6], K = 1
# Output: [1, 2, 3, 4, 5, 6]

# Example 4:
# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], K = 10 
# Output: [8, 7, 6, 5, 4, 3, 2, 1]

# **************************
# Python Solution:
# **************************

def reverse_array_in_groups(arr, K):
    """
    Function to reverse every subarray formed by consecutive K elements.
    """
    
    # If the array is empty or length of array is less than 2, return the original array
    if len(arr) == 0 or len(arr) < 2:
        return arr
    
    # Traverse the array in steps of K
    for start in range(0, len(arr), K):
        # Get the right pointer, ensuring it doesn't go out of bounds
        left = start
        right = min(start + K - 1, len(arr) - 1)

        # Reverse the current group of K elements
        while left < right:
            # Swap elements at left and right pointers
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


# Example usage:

# Test case 1
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
K = 3
print(f"Original Array: {arr1}")
reversed_arr = reverse_array_in_groups(arr1, K)
print(f"Array after reversing in groups of {K}: {reversed_arr}")

# Test case 2: When K > len(arr)
arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
K2 = 10
print(f"\nOriginal Array: {arr2}")
reversed_arr2 = reverse_array_in_groups(arr2, K2)
print(f"Array after reversing in groups of {K2}: {reversed_arr2}")

# Test case 3: When K = 1 (No change expected)
arr3 = [1, 2, 3, 4, 5, 6]
K3 = 1
print(f"\nOriginal Array: {arr3}")
reversed_arr3 = reverse_array_in_groups(arr3, K3)
print(f"Array after reversing in groups of {K3}: {reversed_arr3}")
