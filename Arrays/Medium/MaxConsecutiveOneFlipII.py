"""
     * <pre>
     * !Maximum Consecutive Ones After Flipping Zeroes
     * Given a binary array arr[] and an integer k, find the maximum length of a subarray
     * containing all ones after flipping at most k zeroes to 1's.
     *
     * Examples: Input: arr[] = {1, 0, 1}, k = 1
     * Output: 3
     * Explanation: By flipping the zero at index 1, all the array elements become one.
     *
     * Input: arr[] = {1, 0, 0, 1, 0, 1, 0, 1}, k = 2
     * Output: 5
     * Explanation: By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all 1's.
     *
     * !Approach: Using Sliding Window Technique - O(n) Time and O(1) Space
     * </pre>
"""


def maximumConsecutiveOneAfterFlippingII(nums: list, k: int):
    maxLength = 0

    for i in range(0, len(nums)):

        zeroCount = 0

        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeroCount += 1

            if zeroCount <= k:
                maxLength = max(maxLength, (j - i + 1))
    return maxLength


if __name__ == "__main__":
    arr1 = [1, 0, 1]
    print("Expected: 3 == ", maximumConsecutiveOneAfterFlippingII(arr1, 1))

    arr2 = [1, 0, 0, 1, 0, 1, 0, 1]
    print("Expected: 5 == ", maximumConsecutiveOneAfterFlippingII(arr2, 2))

    arr3 = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
    print("Expected: 7 == ", maximumConsecutiveOneAfterFlippingII(arr3, 2))
