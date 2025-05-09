# * Finding the sum of digits of a number until the sum becomes a single digit.

# Given an integer n, we need to repeatedly find the sum of its digits until
# the result becomes a single-digit number.

# Examples:
# Input: n = 1234
# Output: 1
# Explanation:
# Step 1: 1 + 2 + 3 + 4 = 10
# Step 2: 1 + 0 = 1

# Input: n = 5674
# Output: 4
# Explanation:
# Step 1: 5 + 6 + 7 + 4 = 22
# Step 2: 2 + 2 = 4


def find_sum_of_digits(n):
    """
    Find the sum of digits of the number and reduce it to a single digit.
    The process keeps summing the digits until we get a single digit result.

    Parameters:
    n (int): The number to process.

    Returns:
    int: The final single digit sum.
    """
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    
    return n


def main():
    # Test cases
    arr1 = 1234
    arr2 = 5674
    arr3 = 9684
    arr4 = 123
    arr5 = 2**31-1  # Simulating Integer.MAX_VALUE in Python
    arr6 = 10 + (-5) + 20  # Sum = 10 + (-5) + 20 = 25

    print("The sum of digit is:")
    print(find_sum_of_digits(arr1))  # Output: 1
    print(find_sum_of_digits(arr2))  # Output: 4
    print(find_sum_of_digits(arr3))  # Output: 8
    print(find_sum_of_digits(arr4))  # Output: 6
    print(find_sum_of_digits(arr5))  # Output: 9
    print(find_sum_of_digits(arr6))  # Output: 7


if __name__ == "__main__":
    main()
