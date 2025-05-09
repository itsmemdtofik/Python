# ! Missing ranges of numbers.
# 
# You have an inclusive interval [lower, upper] and a sorted array of unique
# integers arr[], all of which lie within this interval. A number x is
# considered missing if x is in the range [lower, upper] but not present in
# arr. Your task is to return the smallest set of sorted ranges that includes
# all missing numbers, ensuring no element from arr is within any range, and
# every missing number is covered exactly once.
# 
# Examples
# 
# Input: arr[] = [14, 15, 20, 30, 31, 45], lower = 10, upper = 50
# Output: [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]
# Explanation: These ranges represent all missing numbers between 10 and 50 not
# present in the array
# 
# Input: arr[] = [-48, -10, -6, -4, 0, 4, 17], lower = -54, upper = 17
# Output: [[-54, -49], [-47, -11], [-9, -7], [-5, -5], [-3, -1], [1, 3],
# [5,16]]
# Explanation: These ranges represent all missing numbers between -54 and 17
# not present in the array.

from typing import List

class MissingRangesOfNumber:

    @staticmethod
    def find_missing_ranges(arr: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        Key Idea:
        - Check the range before the first element of arr[].
        - Check the gaps between consecutive elements in arr[].
        - Check the range after the last element of arr[].
        """
        result = []

        # Handle the range before the first element in the array
        if not arr:
            result.append([lower, upper])
            return result

        if arr[0] > lower:
            result.append([lower, arr[0] - 1])

        # Handle the gap between consecutive elements in the array
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                result.append([arr[i - 1] + 1, arr[i] - 1])

        # Handle the range after the last element in the array
        if arr[-1] < upper:
            result.append([arr[-1] + 1, upper])

        return result

    @staticmethod
    def another_find_missing_ranges(arr: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        Another method:
        - Track the current number starting at lower.
        - For each number in arr[], if current < num, add range [current, num-1].
        - Update current to num + 1.
        - After the loop, check if any range from current to upper.
        """
        result = []

        current = lower

        for num in arr:
            if num > current:
                result.append([current, num - 1])
            current = num + 1

        if current <= upper:
            result.append([current, upper])

        return result

    @staticmethod
    def print_missing_ranges(result: List[List[int]]):
        for start, end in result:
            if start == end:
                print(start)
            else:
                print(f"[{start}, {end}]")

def main():
    arr1 = [14, 15, 20, 30, 31, 45]
    lower1, upper1 = 10, 50
    missing_ranges1 = MissingRangesOfNumber.find_missing_ranges(arr1, lower1, upper1)
    MissingRangesOfNumber.print_missing_ranges(missing_ranges1)

    print()  # For separating outputs

    arr2 = [-48, -10, -6, -4, 0, 4, 17]
    lower2, upper2 = -54, 17
    missing_ranges2 = MissingRangesOfNumber.find_missing_ranges(arr2, lower2, upper2)
    MissingRangesOfNumber.print_missing_ranges(missing_ranges2)

if __name__ == "__main__":
    main()
