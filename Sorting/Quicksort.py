import random
from typing import List

class QuickSortClass:
    @staticmethod
    def _f_partition(arr: List[int], low: int, high: int) -> int:
        i = low
        j = high + 1
        pivot = arr[low]  # Use the first element to pivot

        while i <= j:
            i += 1
            while i <= high and arr[i] <= pivot:  # Ensure i doesn't exceed high
                i += 1

            j -= 1
            while j >= low and arr[j] > pivot:   # Ensure j doesn't go below low
                j -= 1

            """
            This swapping is for arranging the elements which are lesser than pivot.
            And also the elements which are greater than pivot.
            The elements which are greater than pivot will come on the right side.
            The elements which are smaller than pivot will come on the left side.
            Swap elements at i and j
            """
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        """
        This swapping is for finding the pivot element and exchanging it with the j
        position element.
        Swap pivot with arr[j] so that pivot is in its correct position.
        """
        arr[low], arr[j] = arr[j], arr[low]

        return j  # Return the index of the pivot element

    @staticmethod
    def _f_quick_sort(arr: List[int], low: int, high: int) -> List[int]:
        if low < high:
            j = QuickSortClass._f_partition(arr, low, high)  # Partition the array
            QuickSortClass._f_quick_sort(arr, low, j - 1)    # Recursively Sort the left side
            QuickSortClass._f_quick_sort(arr, j + 1, high)  # Recursively Sort the right side
        return arr

    @staticmethod
    def run_test_cases() -> None:
        test_cases = []

        # Adding complex test cases
        test_cases.append([2, 7, 1, 15, 5, 20, 40])  # Random unsorted array
        test_cases.append([1])                       # Single element
        test_cases.append([2, 1])                   # Two elements unsorted
        test_cases.append([1, 2])                   # Two elements sorted
        test_cases.append([10, 16, 8, 12, 15, 6, 3, 9, 5, 100])  # Random unsorted array
        test_cases.append([1, 2, 3, 4, 5, 6, 7, 8])  # Already sorted array
        test_cases.append([8, 7, 6, 5, 4, 3, 2, 1])  # Reverse sorted array
        test_cases.append([4, 2, 2, 8, 3, 3, 1])     # Array with duplicates

        # Generating additional complex test cases dynamically
        for _ in range(92):
            size = random.randint(10, 100)  # Random size between 10 and 100
            random_array = [random.randint(-500, 499) for _ in range(size)]
            test_cases.append(random_array)

        all_tests_passed = True  # Track if all tests pass

        # Running all test cases
        for test_case in test_cases:
            sorted_arr = QuickSortClass._f_quick_sort(test_case.copy(), 0, len(test_case) - 1)

            # Validate if the output is sorted
            if not QuickSortClass.is_sorted(sorted_arr):
                all_tests_passed = False
                print(f"Some test case failed: {test_case}")  # Print the failing test case

        # After all test cases are processed, print the result
        if all_tests_passed:
            print("All test cases passed!")
        else:
            print("Some test cases failed.")

    @staticmethod
    def is_sorted(arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

def main():
    """
    Question: Why do we use the first element as pivot?
    Answer: Using the first element as pivot is simple to implement,
    but can lead to worst-case O(n²) performance if the array is already sorted.
    For better performance with sorted arrays, consider using:
    1. Middle element as pivot
    2. Random element as pivot
    3. Median-of-three partitioning
    """
    QuickSortClass.run_test_cases()
    print("\n---------------------------------------------\n")

if __name__ == "__main__":
    main()