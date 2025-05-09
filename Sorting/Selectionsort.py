import random
from typing import List

class SelectionSort:
    @staticmethod
    def _f_selection_sort(arr: List[int]) -> List[int]:
        """
        Performs selection sort on the input array.
        Selection sort works by repeatedly finding the minimum element
        from unsorted part and putting it at the beginning.
        """
        for i in range(len(arr) - 1):
            min_idx = i
            
            # Find the index of the minimum element in remaining unsorted array
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap the found minimum element with the first element of unsorted part
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr

    @staticmethod
    def run_test_cases() -> None:
        """
        Runs comprehensive test cases for selection sort, including:
        - Empty array
        - Single element array
        - Small arrays
        - Already sorted arrays
        - Reverse sorted arrays
        - Arrays with duplicates
        - Randomly generated large arrays
        """
        test_cases = []
        
        # Adding standard test cases
        test_cases.append([])  # Empty array
        test_cases.append([1])  # Single element
        test_cases.append([2, 1])  # Two elements unsorted
        test_cases.append([1, 2])  # Two elements sorted
        test_cases.append([10, 16, 8, 12, 15, 6, 3, 9, 5, 100])  # Random unsorted
        test_cases.append([1, 2, 3, 4, 5, 6, 7, 8])  # Already sorted
        test_cases.append([8, 7, 6, 5, 4, 3, 2, 1])  # Reverse sorted
        test_cases.append([4, 2, 2, 8, 3, 3, 1])  # With duplicates

        # Generating 92 additional random test cases
        for _ in range(92):
            size = random.randint(10, 100)  # Arrays of size 10-100
            random_array = [random.randint(-500, 499) for _ in range(size)]
            test_cases.append(random_array)

        # Running all test cases
        test_case_number = 1
        for test_case in test_cases:
            print(f"Test Case {test_case_number}:")
            print(f"Input: {test_case}")
            
            # Sort a copy to preserve original test case
            sorted_arr = SelectionSort._f_selection_sort(test_case.copy())
            print(f"Output: {sorted_arr}")

            # Validate sorting
            if SelectionSort.is_sorted(sorted_arr):
                print("Result: Pass\n")
            else:
                print("Result: Fail\n")

            test_case_number += 1

    @staticmethod
    def is_sorted(arr: List[int]) -> bool:
        """
        Helper function to check if an array is sorted in ascending order.
        """
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

def main():
    """
    Main function to demonstrate selection sort.
    Question: Why does selection sort have O(n²) time complexity?
    Answer: Because it uses two nested loops - an outer loop that runs n times
    and an inner loop that runs n-i times, resulting in n*(n-1)/2 comparisons,
    which simplifies to O(n²) in Big-O notation.
    """
    SelectionSort.run_test_cases()

if __name__ == "__main__":
    main()