# ! Printing the subarrays.
# Given an array, print all possible subarrays of that array.
# A subarray is any contiguous part of the array.

# Example:
# Input: arr = [1, 2, 3, 4, 5]
# Output:
# 1 12 123 1234 12345
# 2 23 234 2345
# 3 34 345
# 4 45
# 5

def print_subarrays(arr):
    """
    Function to print all possible subarrays of the given array.
    A subarray is any contiguous part of the array.
    """
    n = len(arr)

    # Loop through all the possible starting points
    for start in range(n):
        # Loop through all the possible ending points from start to n
        for end in range(start, n):
            # Print the subarray from arr[start] to arr[end]
            for i in range(start, end + 1):
                print(arr[i], end="")
            print(" ", end="")
        print()  # New line after each set of subarrays

def main():
    arr = [1, 2, 3, 4, 5]
    print_subarrays(arr)

if __name__ == "__main__":
    main()
