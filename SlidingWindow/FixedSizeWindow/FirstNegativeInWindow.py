"""
	 * <pre>
	 * !First negative integer in every window of size k
	 * Given an array and a positive integer k, find the first negative integer for
	 * each window(contiguous subarray) of size k.
	 * If a window does not contain a negative integer, then print 0 for that window.
	 *
	 * Input: arr[] = [-8, 2, 3, -6, 1] , k = 2
	 * Output: [-8, 0, -6, -6]
	 * Explanation: First negative integer for each window of size 2
	 * [-8, 2] = -8
	 * [2, 3]= 0 (does not contain a negative integer)
	 * [3, -6] = -6
	 * [-6, 10] = -6
	 * </pre>

"""
from collections import deque


def firstNegative(nums: int, window: int):
    result = []
    for i in range(len(nums) - window + 1):
        found = False
        for j in range(i, i + window):
            if nums[j] < 0:
                result.append(nums[j])
                found = True
                break
        if not found:
            result.append(0)
    return result


# Optimized sliding window version using deque
def slidingWindow(nums, window):
    result = []
    queue = deque()

    for i in range(len(nums)):
        # Remove indices out of the current window
        while queue and queue[0] < i - window + 1:
            queue.popleft()

        # If current number is negative, store its index
        if nums[i] < 0:
            queue.append(i)

        # When the window is fully formed
        if i >= window - 1:
            if queue:
                result.append(nums[queue[0]])  # First negative
            else:
                result.append(0)  # No negative
    return result


if __name__ == "__main__":
    nums = [-8, 2, 3, -6, 1]
    window = 2
    result = firstNegative(nums, window)
    print("First Negative Integer in Window are:", result)

    nums1 = [12, -1, -7, 8, -15, 30, 16, 28]
    window1 = 3
    result1 = slidingWindow(nums1, window1)
    print("First Negative Integer in Window are:", result1)
