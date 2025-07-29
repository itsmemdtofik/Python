"""
     * <pre>
     * !Minimum Sum Subarray
     * Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
     *
     * Input: nums = [3, 8, 2, 5, 7, 6, 12], k = 4
     * Output: 18
     * Explanation: Subarray [3, 8, 2, 5] has the maximum sum of 18.
     *
     * </pre>
"""


def minimumSum(nums: int, K: int):
    """
    This is a sliding window solution but not fully optimized,
    because i + window - 1 can overflow (if not carefully handled).
    """
    if nums is None or len(nums) == 0:
        return 0

    left = 0
    right = 0
    currentSum = 0
    minimum = float('inf')

    while right < len(nums):
        currentSum += nums[right]
        window = (right - left) + 1

        if window < K:
            right += 1
        elif window == K:
            minimum = min(minimum, currentSum)
            currentSum -= nums[left]
            left += 1
            right += 1

    return minimum


def slidingWindow(nums: int, window: int):
    """
    This is a correct sliding window technique using safe subtraction with (i - window).
    Time complexity: O(n)
    """
    if nums is None or window <= 0 or window > len(nums):
        return 0

    currentSum = sum(nums[:window])
    minSum = currentSum

    for i in range(window, len(nums)):
        currentSum = currentSum - nums[i - window] + nums[i]
        minSum = min(minSum, currentSum)

    return minSum


if __name__ == "__main__":
    nums = [3, 8, 2, 5, 7, 6, 12]
    k = 4

    result = minimumSum(nums, k)
    print("Minimum sum of subarray of size", k, "is:", result)

    nums1 = [3, 8, 2, 5, 7, 6, 12]
    k1 = 4

    result1 = slidingWindow(nums1, k1)
    print("Minimum sum of subarray of size", k1, "using sliding window is:", result1)
