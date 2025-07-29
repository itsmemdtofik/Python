"""
     * <pre>
     * !Sum of all subarrays of size K
     * Given an array arr[] and an integer K, the task is to calculate the sum of all subarrays of size K.
     *
     * Input: arr[] = {1, 2, 3, 4, 5, 6}, K = 3
     * Output: 6 9 12 15
     * Explanation: All subarrays of size k and their sum:
     * Subarray 1: {1, 2, 3} = 1 + 2 + 3 = 6
     * Subarray 2: {2, 3, 4} = 2 + 3 + 4 = 9
     * Subarray 3: {3, 4, 5} = 3 + 4 + 5 = 12
     * Subarray 4: {4, 5, 6} = 4 + 5 + 6 = 15
     * </pre>
"""


# This is not a sliding window technique caz of O(n * k)
def sumOfAllSubarray(nums: int, window: int):
    result = []

    for i in range(len(nums) - window + 1):
        currentSum = 0
        for j in range(i, i + window):
            currentSum += nums[j]
        result.append(currentSum)

    return result


# Let's solve this using the sliding window O(n)
def slidingWindow(nums: int, window: int):
    currentSum = 0
    result = []

    # sum of first window
    for i in range(window):
        currentSum += nums[i]
    result.append(currentSum)

    # slide the window
    for i in range(window, len(nums)):
        currentSum = currentSum - nums[i - window] + nums[i]
        result.append(currentSum)

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    window = 3

    result = sumOfAllSubarray(nums, window)
    print("Sum of all subarrays of size k are:", result)

    nums1 = [1, 2, 3, 4, 5, 6]
    window1 = 3

    result1 = slidingWindow(nums1, window1)
    print("Sum of all subarrays of size k using sliding window are:", result1)
