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


def maximumConsecutiveOneAfterFlipping(nums: list, k: int):
    n = len(nums)
    left = right = maxLen = zeroCount = 0

    while right < len(nums):

        if nums[right] == 0:
            zeroCount += 1

        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1

        maxLen = max(maxLen, right - left + 1)
        print(f"Right = {right}, left = {left}, zeros = {zeroCount}, maxLength = {maxLen}")
        right += 1

    return maxLen


if __name__ == "__main__":
    arr1 = [1, 0, 1]
    print("Expected: 3 == ", maximumConsecutiveOneAfterFlipping(arr1, 1))

    arr2 = [1, 0, 0, 1, 0, 1, 0, 1]
    print("Expected: 5 == ", maximumConsecutiveOneAfterFlipping(arr2, 2))

    arr3 = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
    print("Expected: 7 == ", maximumConsecutiveOneAfterFlipping(arr3, 2))
