# ! Move all zeros to end of an array.
# 
# Given an array of integers arr[], the task is to move all the zeros to 
# the end of the array while maintaining the relative order of all non-zero elements.
# 
# Examples: 
# 
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# 
# Input: arr[] = [10, 20, 30]
# Output: arr[] = [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# 
# Input: arr[] = [0, 0]
# Output: arr[] = [0, 0]
# Explanation: No change in array as there are all 0s.

from typing import List

class MoveAllZerosToEnd:

    @staticmethod
    def move_zeros_to_end(arr: List[int]) -> List[int]:
        """
        Method 1: Move all zeros to the end while keeping non-zero elements in their relative order.
        This method creates a new array, `zero[]`, and copies non-zero elements into it while 
        placing zeros at the end.
        """
        if len(arr) == 0 or len(arr) == 1:
            return arr
        
        zero = [0] * len(arr)
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                zero[j] = arr[i]
                j += 1
        
        return zero

    @staticmethod
    def push_zeros_to_end(arr: List[int]) -> List[int]:
        """
        Method 2: In-place solution: Push all zeros to the end of the array
        while maintaining the order of non-zero elements.
        """
        if len(arr) == 0:
            return arr
        
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        
        while j < len(arr):
            arr[j] = 0
            j += 1
        
        return arr

    @staticmethod
    def push_to_end(arr: List[int]) -> List[int]:
        """
        Method 3: In-place swapping solution to push zeros to the end.
        Swaps non-zero elements to the beginning of the array.
        """
        if len(arr) <= 1:
            return arr
        
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        
        return arr

    @staticmethod
    def test_move_zeros():
        """
        Test the methods with multiple test cases.
        """
        test_arrays = [
            [0],  # Edge case: empty array
            [5],  # Edge case: single element array
            [5, 5],  # Case: both elements are the same
            [1, 2, 3, 4, 5],  # Normal case: distinct elements
            [10, 5, 2, 10, 5],  # Case: some duplicate elements
            [2, 2, 2, 2, 2],  # Case: all elements are the same
            [1, -4, 3, -6, 7, 0],  # Containing negative elements
            [10, 3, 5, 6, 20],
            [-10, -3, -5, -6, -20],  # Containing negative elements
            [1, 2, 0, 4, 3, 0, 5, 0],  # Example case
        ]

        for arr in test_arrays:
            result = MoveAllZerosToEnd.push_to_end(arr)  # Using the push_to_end method
            print(f"Moved to end: {result}")


def main():
    MoveAllZerosToEnd.test_move_zeros()

if __name__ == "__main__":
    main()
