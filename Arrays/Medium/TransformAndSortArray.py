"""
     * <pre>
     * !Sort an array after applying the given equation
     * Given an integer array arr[] sorted in ascending order, along with three integers: A, B, and C.
     * The task is to transform each element x in the array using the quadratic function A*(x^2) + B*x + C.
     * After applying this transformation to every element, return the modified array in sorted order.
     *
     * @param Examples:
     * Input: arr[] = [-4, -2, 0, 2, 4], A = 1, B = 3, C = 5
     * Output: [3, 5, 9, 15, 33]
     * Explanation: After applying f(x) = 1 * x2 + 3 * x + 5 to each x, we get [9, 3, 5, 15, 33].
     * After sorting this array, the array becomes [3, 5, 9, 15, 33].
     *
     * Input: arr[] = [-3, -1, 2, 4], A = -1, B = 0, C = 0
     * Output: [-16, -9, -4, -1]
     * Explanation: After applying f(x) = -1*x2 to each x, we get [-9, -1, -4, -16 ].
     * After sorting this array, the array becomes  [-16, -9, -4, -1].
     *
     * Input: arr[] = [-1, 0, 1, 2, 3, 4], A = -1, B = 2, C = -1
     * Output: [-9, -4, -4, -1, -1, 0]
     *
     * !Approach: Apply the Equation and Sort – O(n*log(n)) Time and O(1) Space
     * The idea is to directly transform each element in the array, i.e. for each element x in arr[],
     * apply the given equation A*x2 + B*x + C in-place and then simply sort the array in ascending order.
     * </pre>
"""
from typing import List


class TransformAndSortArray:

    @staticmethod
    def equation(x: int, A: int, B: int, C: int) -> int:
        return A * x * x + B * x + C

    @staticmethod
    def transformAndSort(nums: List[int], A: int, B: int, C: int) -> List[int]:
        n = len(nums)
        transformed = [0] * n

        # Apply the transformation and store in array
        for i in range(n):
            transformed[i] = TransformAndSortArray.equation(nums[i], A, B, C)

        # Sort the transformed values
        transformed.sort()

        return transformed


if __name__ == "__main__":
    print("Expected: [3, 5, 9, 15, 33] == ", TransformAndSortArray.transformAndSort([-4, -2, 0, 2, 4], 1, 3, 5))
    print("Expected: [-16, -9, -4, -1] == ", TransformAndSortArray.transformAndSort([-3, -1, 2, 4], -1, 0, 0))
    print("Expected: [-9, -4, -4, -1, -1, 0] == ",
          TransformAndSortArray.transformAndSort([-1, 0, 1, 2, 3, 4], -1, 2, -1))
