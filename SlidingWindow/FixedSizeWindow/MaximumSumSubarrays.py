"""
     * <pre>
     * !Maximum Sum Subarray
     * Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
     *
     * Input: nums = [2, 1, 5, 1, 3, 2], k = 3
     * Output: 9
     * Explanation: Subarray [5, 1, 3] has the maximum sum of 9.
     *
     * </pre>
"""


# This is sliding window solution but not follow fully caz i + window - 1 can overflow
def maximumSum(nums: int, window: int):
    if nums is None or window <= 0 or window > len(nums):
        return 0

    currentSum = 0
    for i in range(window):
        currentSum += nums[i]

    maxx = currentSum

    for i in range(1, len(nums) - window + 1):
        currentSum = currentSum - nums[i - 1] + nums[i + window - 1]
        if currentSum > maxx:
            maxx = currentSum

    return maxx


# This is another sliding window solution which follow fully caz Uses i - window for safe subtraction
def slidingWindow(nums, window):
    if nums is None or window <= 0 or window > len(nums):
        return 0

    currentSum = 0
    for i in range(window):
        currentSum += nums[i]

    maxSum = currentSum

    for i in range(window, len(nums)):
        currentSum = currentSum - nums[i - window] + nums[i]
        maxSum = max(maxSum, currentSum)

    return maxSum


if __name__ == "__main__":
    num = [3, 8, 2, 5, 7, 6, 12]
    k = 4

    result = maximumSum(num, k)
    print("Maximum sum of subarray of size", k, "is:", result)

    num1 = [3, 8, 2, 5, 7, 6, 12]
    k1 = 4

    result1 = slidingWindow(num1, k1)
    print("Maximum sum of subarray of size", k1, "using sliding window is:", result1)
