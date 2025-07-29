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


def minimumSum(nums:int, window:int):
    """
    This is a sliding window solution but not fully safe,
    since it uses i + window - 1 indexing directly.
    Time Complexity: O(n)
    """
    if nums is None or len(nums) == 0:
        return 0

    currentSum = 0

    # Sum of first window
    for i in range(window):
        currentSum += nums[i]

    minimum = currentSum

    # Slide the window forward
    for i in range(1, len(nums) - window + 1):
        current_sum = currentSum - nums[i - 1] + nums[i + window - 1]
        minimum = min(minimum, current_sum)

    return minimum


def slidingWindow(nums:int, window:int):
    """
    This is another sliding window solution which follows the proper technique.
    It uses safe subtraction via (i - window) index.
    Time Complexity: O(n)
    """
    if nums is None or window <= 0 or window > len(nums):
        return 0

    currentSum = sum(nums[:window])
    minSum = currentSum

    # Move the window forward
    for i in range(window, len(nums)):
        currentSum = currentSum - nums[i - window] + nums[i]
        minSum = min(minSum, currentSum)

    return minSum


num = [3, 8, 2, 5, 7, 6, 12]
k = 4

result = minimumSum(num, k)
print("Minimum sum of subarray of size", k, "is:", result)

nums1 = [3, 8, 2, 5, 7, 6, 12]
k1 = 4

result1 = slidingWindow(nums1, k1)
print("Minimum sum of subarray of size", k1, "using sliding window is:", result1)
