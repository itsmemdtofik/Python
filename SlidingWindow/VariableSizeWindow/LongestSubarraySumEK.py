"""
     * <pre>
     * !Longest Subarray With Sum K
     * Given an array arr[] of size n containing integers, the task is to
     * find the length of the longest subarray having sum equal to the given value k.
     *
     * Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
     * Output: 6
     * Explanation:
     * Subarrays with sum = 15 are
     * [5, 2, 7, 1], [10, 5] and
     * [10, 5, 2, 7, 1, -10].
     * The length of the longest subarray with a sum of 15 is 6.
     *
     * Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
     * Output: 5
     * Explanation:
     * Only subarray with sum = 15 is [-5, 8, -14, 2, 4] of length 5.
     *
     * Input: arr[] = [10, -10, 20, 30], k = 5
     * Output: 0
     * Explanation: No subarray with sum = 5 is present in arr[].
     *
     * </pre>
"""


def longestSubarraySumEK(nums:int, K:int):
    """
    This is not a sliding window solution because of O(n^2) time complexity.
    Brute-force approach: check all subarrays.
    """
    result = 0

    for left in range(len(nums)):
        currentSum = 0
        for right in range(left, len(nums)):
            currentSum += nums[right]

            if currentSum == K:
                subarrayLength = right - left + 1  # find subarray length and update result
                result = max(result, subarrayLength)

    return result


def slidingWindow(nums:int, K:int):
    """
    Let's solve it using the sliding window O(n)
    Note: Sliding window works only with Non-Negative Integers.
    Why Only Non-Negative?
    If negative numbers exist, shrinking the window might skip valid subarrays.
    """
    left = 0
    currentSum = 0
    maxLen = 0

    for right in range(len(nums)):
        currentSum += nums[right]

        while currentSum > K:
            currentSum -= nums[left]  # Shrink window if sum exceeds k
            left += 1

        if currentSum == K:
            maxLen = max(maxLen, right - left + 1)

    return maxLen


def prefixAndHashing(nums:int, K:int):
    """
    Let's solve this using Prefix Sum + Hashing.
    This works for all integers, including negatives.
    """
    freqMap = {}  # Stores prefix_sum -> first index
    prefixSum = 0
    maxLen = 0

    for right in range(len(nums)):
        prefixSum += nums[right]

        if prefixSum == K:
            maxLen = right + 1

        if (prefixSum - K) in freqMap:
            maxLen = max(maxLen, right - freqMap[prefixSum - K])
        else:
            freqMap.setdefault(prefixSum, right)  # Store first occurrence

    return maxLen


if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, -10]
    k = 15

    window = longestSubarraySumEK(nums, k)
    print("Longest Subarray with sum equal to K is:", window)

    nums1 = [1, 2, 3, 4, 5]
    k1 = 9

    window1 = slidingWindow(nums1, k1)
    print("Longest Subarray with sum equal to K using sliding window is:", window1)

    nums2 = [10, 5, 2, 7, 1, -10]
    k2 = 15

    window2 = prefixAndHashing(nums2, k2)
    print("Longest Subarray with sum equal to K using prefix sum and hashing is:", window2)
