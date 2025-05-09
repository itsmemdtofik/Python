import random
from typing import List

class MergeSort:
    @staticmethod
    def _f_conquer(arr: List[int], low: int, mid: int, high: int) -> None:
        """
        Now we will start inserting element into the mergedArr[]
        """
        merged_arr = [0] * (high - low + 1)

        """
        Now we will create two index index1 and index2
        The index1 will start from starting index and index1 will track the first array.
        The index2 will start from (mid + 1) index and index2 will track the second array.
        """
        index1 = low
        index2 = mid + 1

        """
        Now who is tracking the third array which is merged array.
        To track the merged array we will create the mergedIndex for the merged array as well.
        The mergedIndex will start from zero.
        """
        merged_index = 0

        """
        This is for first sub-array = [3, 6, 9] and second sub-array = [2, 5, 8]
        """
        while index1 <= mid and index2 <= high:
            if arr[index1] <= arr[index2]:
                merged_arr[merged_index] = arr[index1]
                merged_index += 1
                index1 += 1
            else:
                merged_arr[merged_index] = arr[index2]
                merged_index += 1
                index2 += 1

        """
        The above while loop will work until we comparing in both array.
        Suppose if the first array get finished and if there is some elements
        remaining in the second array.
        Suppose if the second array get finished and if there is some elements
        remaining in the first array.
        Then we will write two more while loop to cover this.
        """
        while index1 <= mid:
            """
            This is for first sub-array = [3, 6, 9]
            """
            merged_arr[merged_index] = arr[index1]
            merged_index += 1
            index1 += 1

        while index2 <= high:
            """
            This is for second sub-array = [2, 5, 8]
            """
            merged_arr[merged_index] = arr[index2]
            merged_index += 1
            index2 += 1

        """
        Now what we have to do?
        Now we have to copy the elements of merged array into the original array.
        So for that we will iterate using for loop.
        """
        for i in range(len(merged_arr)):
            arr[low + i] = merged_arr[i]

    @staticmethod
    def _f_divide_arr(arr: List[int], low: int, high: int) -> List[int]:
        """
        Our Original array is = [6,3,9,5,2,8]
        If we divide this array via applying mid then we get two sub array.
        The first array contains = [6, 3, 9] -> low to mid
        And second array contains = [5, 2, 8] -> mid + 1 to high.
        And while conquering then these two array gets sorted individually.
        First array become = [3, 6, 9] -> index1 to track this sub array
        Second array becomde = [2, 5, 8] -> index2 to track this second sub array.
        Now we merged these two array into new array called mergedArr.
        To track merged array we create mergedIndex.
        """
        if low < high:
            """
            To calculate mid = low + (high - low) / 2 Because of space complexity we are
            removing this
            """
            mid = low + (high - low) // 2
            MergeSort._f_divide_arr(arr, low, mid)
            MergeSort._f_divide_arr(arr, mid + 1, high)
            MergeSort._f_conquer(arr, low, mid, high)
        return arr

    @staticmethod
    def run_test_cases() -> None:
        test_cases = []

        # Adding complex test cases
        test_cases.append([])  # Empty array
        test_cases.append([1])  # Single element
        test_cases.append([2, 1])  # Two elements unsorted
        test_cases.append([1, 2])  # Two elements sorted
        test_cases.append([10, 16, 8, 12, 15, 6, 3, 9, 5, 100])  # Random unsorted array
        test_cases.append([1, 2, 3, 4, 5, 6, 7, 8])  # Already sorted array
        test_cases.append([8, 7, 6, 5, 4, 3, 2, 1])  # Reverse sorted array
        test_cases.append([4, 2, 2, 8, 3, 3, 1])  # Array with duplicates

        # Generating additional complex test cases dynamically
        for _ in range(92):
            size = random.randint(10, 100)  # Random size between 10 and 100
            random_array = [random.randint(-500, 499) for _ in range(size)]
            test_cases.append(random_array)

        # Running all test cases
        test_case_number = 1
        for test_case in test_cases:
            print(f"Test Case {test_case_number}:")
            print(f"Input: {test_case}")
            sorted_arr = MergeSort._f_divide_arr(test_case.copy(), 0, len(test_case) - 1)
            print(f"Output: {sorted_arr}")

            # Validate if the output is sorted
            if MergeSort.is_sorted(sorted_arr):
                print("Result: Pass\n")
            else:
                print("Result: Fail\n")

            test_case_number += 1

    @staticmethod
    def is_sorted(arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

if __name__ == "__main__":
    """
    Question: Why do we need to make copies of the test cases before sorting?
    Answer: Because in Python, lists are mutable objects passed by reference.
    If we don't make a copy, we would modify the original test case array,
    which would affect subsequent test runs or comparisons.
    """
    MergeSort.run_test_cases()