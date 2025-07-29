"""
     * <pre>
     * !Maximum subarray size having all subarrays sums less than k
     * Given an array of positive integers arr[] of size n, and an integer k.
     * The task is to find the maximum subarray size such that all subarrays of that size have sum less than or equals to k.
     *
     * Input :  arr[] = [1, 2, 3, 4], k = 8.
     * Output : 2
     * Explanation: Following are the sum of subarray of size 1 to 4.
     * Sum of subarrays of size 1: 1, 2, 3, 4.
     * Sum of subarrays of size 2: 3, 5, 7.
     * Sum of subarrays of size 3: 6, 9.
     * Sum of subarrays of size 4: 10.
     * So, maximum subarray size such that all subarrays of that size have the sum of elements less than 8 is 2.
     *
     * Input:  arr[] = [1, 2, 10, 4], k = 8.
     * Output : -1
     * Explanation: There is an array element (10) with value greater than k, so subarray sum cannot be less than k.
     * </pre>
"""


def longestSubarraySumLEK(nums:int, K:int):
    """
    This is NOT a sliding window solution due to O(n^2) complexity.
    Brute-force approach: try all window sizes from largest to smallest.
    """

    # Check if any single element is greater than K
    for num in nums:
        if num > K:
            return -1

    # Try all window sizes from len(nums) down to 1
    for i in range(len(nums), 0, -1):
        isValid = True
        windowSum = sum(nums[:i])  # First window

        if windowSum > K:
            isValid = False

        # Slide the window across the array
        for j in range(i, len(nums)):
            windowSum = windowSum + nums[j] - nums[j - i]
            if windowSum > K:
                isValid = False
                break

        if isValid:
            return i

    return -1


def slidingWindow(nums:int, K:int):
    """
    Brute-force approach to find the maximum size such that all subarrays of that size have sum < K
    Time Complexity: O(n^2)
    """
    if any(num >= K for num in nums):
        return -1

    n = len(nums)

    for size in range(n, 0, -1):
        isValid = True
        windowSum = sum(nums[:size])

        if windowSum >= K:
            isValid = False

        for j in range(size, n):
            windowSum = windowSum + nums[j] - nums[j - size]
            if windowSum >= K:
                isValid = False
                break

        if isValid:
            return size

    return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    K = 8

    result = longestSubarraySumLEK(nums, K)
    print("Maximum subarray size such that all subarrays of that size have the sum of elements less than", K, "is:", result)

    nums1 = [1, 2, 10, 4]
    K1 = 14

    result1 = slidingWindow(nums1, K1)
    print("Maximum subarray size such that all subarrays of that size have the sum of elements less than", K1, "is:", result1)
