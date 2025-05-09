# **************************
# Problem: Finding the Second Largest Element in an Array
# **************************

# Given an array of integers, the task is to find the second largest element in the array.
# If there is no second largest element (for example, when all elements are the same), return None.

# **************************
# Python Solution:
# **************************

def second_largest(arr):
    """
    This method finds the second largest element in an array by first determining the largest element,
    and then finding the largest element smaller than the first.
    """

    if not arr or len(arr) < 2:
        return None  # Return None if array is empty or has only one element

    first = float('-inf')  # Initialize the first (largest) to negative infinity
    second = float('-inf')  # Initialize the second to negative infinity

    # Loop through the array to find the largest element
    for num in arr:
        first = max(first, num)

    # Loop through the array to find the second largest element
    for num in arr:
        if num < first:
            second = max(second, num)

    # If second is still negative infinity, it means no second largest element was found
    if second == float('-inf'):
        return None
    
    return second


def second_large(arr):
    """
    This method finds the second largest element in the array by comparing elements and updating the 
    first and second largest values in one pass.
    """

    first = float('-inf')
    second = float('-inf')

    # Loop through the array to update first and second largest elements
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    # If second is still negative infinity, return None
    if second == float('-inf'):
        return None

    return second


# Test cases
test_arrays = [
    [],  # Edge case: empty array
    [5],  # Edge case: single element array
    [5, 5],  # Case: both elements are the same
    [1, 2, 3, 4, 5],  # Normal case: distinct elements
    [10, 5, 2, 10, 5],  # Case: some duplicate elements
    [2, 2, 2, 2, 2]  # Case: all elements are the same
]

for arr in test_arrays:
    result = second_large(arr)
    print(f"Array: {arr} => Second Largest: {'None' if result is None else result}")
