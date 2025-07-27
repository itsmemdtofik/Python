"""
     * <pre>
     * !Minimum Swaps required to group all 1's together
     * Given an array of 0's and 1's, we need to write a program to
     * find the minimum number of swaps required to group all 1's present in the array together.
     *
     * @param Examples:
     * Input: arr[] = [1, 0, 1, 0, 1]
     * Output: 1
     * Explanation: Only 1 swap is required to group all 1's together. Swapping index 1 with 4 will
     * give arr[] = [1, 1, 1, 0, 0]
     *
     * Input: arr[] = [1, 1, 0, 1, 0, 1, 1]
     * Output: 2
     * Explanation: Only 2 swap is required to group all 1's together. Swapping index 0 with 2 and
     * 1 with 4 will  give arr[] = [0, 0, 1, 1, 1, 1, 1]
     *
     * Input: arr[] = [0, 0, 0]
     * Output: -1
     * Explanation: No 1s are present in the array, so return -1.
     *
     * !Approach: Using Nested loops - O(n^2) Time and O(n) Space
     * A simple solution is to first count total number of 1’s  in the array.
     * Suppose this count is x, now we need to find the subarray of length x with maximum number of 1’s.
     * And minimum swaps required will be the number of 0’s in this subarray of length x.
     * </pre>
"""


def minimumSwap(nums: list[int]) -> int:
    countOne = i = 0
    n = len(nums)
    minimumSwapSoFar = float('inf')

    for num in nums:
        if num == 1:
            countOne += 1

    if countOne == 0:
        return -1

    for i in range(n - countOne + 1):

        count = 0
        for j in range(i, i + countOne):

            if nums[j] == 1:
                count += 1

        minimumSwapSoFar = min(minimumSwapSoFar, countOne - count)

    return minimumSwapSoFar


nums1 = [1, 0, 1, 0, 1]
print(f"Minimum Swaps To Group All One's : {minimumSwap(nums1)}")
