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
def maximumSum(nums, K):
    if nums is None or len(nums) == 0:
        return 0

    left = 0
    right = 0
    currentSum = 0
    maxx = float('-inf')

    while right < len(nums):
        currentSum += nums[right]
        window = (right - left) + 1

        if window < K:
            right += 1
        elif window == K:
            maxx = max(maxx, currentSum)
            currentSum -= nums[left]
            left += 1
            right += 1

    return maxx


# This is another sliding window solution which follow fully caz Uses i - window for safe subtraction
def slidingWindow(nums, window):
    if nums is None or window <= 0 or window > len(nums):
        return 0

    currentSum = sum(nums[:window])
    maxSum = currentSum

    for i in range(window, len(nums)):
        currentSum = currentSum - nums[i - window] + nums[i]
        maxSum = max(maxSum, currentSum)

    return maxSum


if __name__ == "__main__":
    nums = [3, 8, 2, 5, 7, 6, 12]
    k = 4

    result = maximumSum(nums, k)
    print("Maximum sum of subarray of size", k, "is:", result)

    nums1 = [3, 8, 2, 5, 7, 6, 12]
    k1 = 4

    result1 = slidingWindow(nums1, k1)
    print("Maximum sum of subarray of size", k1, "using sliding window is:", result1)
