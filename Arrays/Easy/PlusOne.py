# ! Adding one to the number represented as a carry of digits.
# 
# Approach:
# 
# Step1: Start from the least significant bit digit (i.e., the last element of an
# array) and add 1.
# Step2: If adding 1 to the last element makes it 10, then set that position to 0
# and propagate the carry. Move this carry 1 to the left element.
# Step3: If there is no carry, the process stops.
# Step4: If you reach the most significant digit (the first element) and still
# have carry, you prepend 1 to the array.
# 
# Example:
# Input = [1, 2, 4]
# Output = [1, 2, 5]
# 
# Input = [9, 9, 9]
# Output = [1, 0, 0, 0]

from typing import List

class PlusOne:

    @staticmethod
    def add_one(arr: List[int]) -> List[int]:
        """
        Adds 1 to the number represented by the array of digits.
        The digits are in order from most significant (at the beginning)
        to least significant (at the end).
        """
        if len(arr) == 0:
            return arr

        carry = 1
        # Traverse the array from the last digit to the first.
        for i in range(len(arr) - 1, -1, -1):
            arr[i] += carry

            if arr[i] == 10:
                arr[i] = 0
                carry = 1  # Propagate the carry
            else:
                carry = 0  # No carry, exit the loop
                break

        # If carry is still left, we need to add it as a new most significant digit.
        if carry == 1:
            result = [1] + arr  # Prepend 1 to the result
            return result

        return arr

    @staticmethod
    def test_plus_one():
        """
        Test the add_one function with multiple test cases.
        """
        test_arrays = [
            [9],  # Single digit
            [1, 2, 4],  # Normal case
            [9, 9, 9],  # Case with carry over
            [1, 7, 8, 9],  # Case with no carry over
            [9, 8, 9, 9],  # Case with multiple carry overs
            []  # Empty array (edge case)
        ]

        for arr in test_arrays:
            result = PlusOne.add_one(arr)
            print(f"After adding one: {result}")


def main():
    PlusOne.test_plus_one()


if __name__ == "__main__":
    main()
