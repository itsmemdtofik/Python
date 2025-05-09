# **************************
# Maximum product of a triplet (subsequence of size 3) in array
# **************************

# Approach:
# Step 1: Find the first, second, and third largest elements in the array.
# Step 2: Return the product of the first * second * third.

# Given an integer array, find the maximum product of a triplet in the array.

# Examples:

# Input:  [10, 3, 5, 6, 20]
# Output: 1200
# Explanation: Multiplication of 10, 6, and 20 gives 1200

# Input:  [-10, -3, -5, -6, -20]
# Output: -90
# Explanation: Multiplication of -10, -6, and -3 gives -90

# Input:  [1, -4, 3, -6, 7, 0]
# Output: 168
# Explanation: Multiplication of 7, 3, and 8 gives 168

def product_of_triplet(arr):
    if len(arr) < 3:
        return 0

    # Initialize the three largest values
    first = second = third = float('-inf')

    # Traverse the array and find the three largest elements
    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != first and num != second:
            third = num

    # If we couldn't find three distinct elements, return 0
    if third == float('-inf'):
        return 0

    return first * second * third


# Example test cases
test_arrays = [
    [],                      # Edge case: empty array
    [5],                     # Edge case: single element array
    [5, 5],                  # Case: both elements are the same
    [1, 2, 3, 4, 5],         # Normal case: distinct elements
    [10, 5, 2, 10, 5],       # Case: some duplicate elements
    [2, 2, 2, 2, 2],         # Case: all elements are the same
    [1, -4, 3, -6, 7, 0],    # Containing negative elements
    [10, 3, 5, 6, 20],       # Test case with distinct elements
    [-10, -3, -5, -6, -20],  # Test case with negative elements
]

# Running the test cases
for arr in test_arrays:
    result = product_of_triplet(arr)
    print(f"Array: {arr} => Product Of Triplet is: {'None' if result == 0 else result}")
