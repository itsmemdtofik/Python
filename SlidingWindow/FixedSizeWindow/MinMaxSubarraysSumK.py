"""
	 * <pre>
	 * !Sum of minimum and maximum elements of all subarrays of size k.
	 * Given an array of both positive and negative integers,
	 * the task is to compute sum of minimum and maximum elements of all sub-array of size k.
	 *
	 * Input : arr[] = {2, 5, -1, 7, -3, -1, -2},  K = 4
	 * Output : 18
	 * Explanation : Subarrays of size 4 are :
	 * {2, 5, -1, 7},   min + max = -1 + 7 = 6
	 * {5, -1, 7, -3},  min + max = -3 + 7 = 4
	 * {-1, 7, -3, -1}, min + max = -3 + 7 = 4
	 * {7, -3, -1, -2}, min + max = -3 + 7 = 4
	 * Missing sub arrays -
	 * {2, -1, 7, -3}
	 * {2, 7, -3, -1}
	 * {2, -3, -1, -2}
	 * {5, 7, -3, -1}
	 * {5, -3, -1, -2}
	 * and few more -- why these were not considered??
	 * Considering missing arrays result coming as 27
	 * Sum of all min & max = 6 + 4 + 4 + 4 = 18
	 *
	 * !Approach: Sliding Window + Dqueue Time Complexity: O(n), Auxiliary Space: O(k)
	 * </pre>
"""
from collections import deque


def sumOfKsubArray(nums: int, window: int):
    """
    Actually this technique is not a sliding window because
    the time complexity of this is O(n * k)
    """

    result = []
    totalSum = 0

    for i in range(len(nums) - window + 1):
        minimum = float('inf')
        maximum = float('-inf')

        for j in range(i, i + window):
            minimum = min(minimum, nums[j])
            maximum = max(maximum, nums[j])

        totalSum += minimum + maximum

    result.append(totalSum)
    return result


def slidingwindow(nums: int, window: int):
    """
    Let's solve this problem using the sliding window technique with O(n) time complexity.
    This uses two deques:
    - queueIn for tracking minimums
    - queueDe for tracking maximums
    """
    totalSum = 0
    queueMax = deque()  # For max
    queueMin = deque()  # For min

    i = 0
    # Initialize first window
    for i in range(window):
        # Maintain elements in increasing order for min queue
        while queueMin and nums[queueMin[-1]] >= nums[i]:
            queueMin.pop()
        # Maintain elements in decreasing order for max queue
        while queueMax and nums[queueMax[-1]] <= nums[i]:
            queueMax.pop()

        queueMin.append(i)
        queueMax.append(i)

    # Process rest of the elements
    for i in range(window, len(nums)):
        # Add current window's min + max
        totalSum += nums[queueMin[0]] + nums[queueMax[0]]

        # Remove indices out of current window
        while queueMin and queueMin[0] <= i - window:
            queueMin.popleft()
        while queueMax and queueMax[0] <= i - window:
            queueMax.popleft()

        # Maintain min deque
        while queueMin and nums[queueMin[-1]] >= nums[i]:
            queueMin.pop()
        # Maintain max deque
        while queueMax and nums[queueMax[-1]] <= nums[i]:
            queueMax.pop()

        queueMin.append(i)
        queueMax.append(i)

    # Add last window's min + max
    totalSum += nums[queueMin[0]] + nums[queueMax[0]]
    return totalSum


if __name__ == "__main__":
    nums = [2, 5, -1, 7, -3, -1, -2]
    window = 4

    result = sumOfKsubArray(nums, window)
    sum_ = slidingwindow(nums, window)

    print("Maximum of subarray of minimum and maximum element:", sum_)
