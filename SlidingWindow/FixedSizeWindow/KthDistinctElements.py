"""
	 * <pre>
	 * !Count Distinct Elements In Every Window of Size K
	 * Given an array arr[] of size n and an integer k, return the count of distinct numbers in all windows of size k.
	 *
	 *
	 * Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
	 * Output: [3, 4, 4, 3]
	 * Explanation: First window is [1, 2, 1, 3], count of distinct numbers is 3.
	 * 				Second window is [2, 1, 3, 4] count of distinct numbers is 4.
	 * 				Third window is [1, 3, 4, 2] count of distinct numbers is 4.
	 * 				Fourth window is [3, 4, 2, 3] count of distinct numbers is 3.
	 *
	 * Input: arr[] = [4, 1, 1], k = 2
	 * Output: [2, 1]
	 * Explanation: First window is [4, 1], count of distinct numbers is 2.
	 * 				Second window is [1, 1], count of distinct numbers is 1.
	 *
	 * !Approach: Sliding Window Technique - O(n) Time and O(k) Space
	 * </pre>

"""
from collections import defaultdict


def countdistinct(nums, window):
    result = []

    for i in range(len(nums) - window + 1):
        seen = set()

        for j in range(i, i + window):
            seen.add(nums[j])

        result.append(len(seen))

    return result


def slidingWindow(nums, window):
    result = []
    map_ = defaultdict(int)

    # Count frequency of elements in the first window
    for i in range(window):
        map_[nums[i]] += 1

    result.append(len(map_))

    for i in range(window, len(nums)):
        # Remove the element going out of the window
        map_[nums[i - window]] -= 1
        if map_[nums[i - window]] == 0:
            del map_[nums[i - window]]

        # Add the new element coming into the window
        map_[nums[i]] += 1

        result.append(len(map_))

    return result


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 4, 2, 3]
    window = 4

    result = countdistinct(nums, window)
    print("The count of distinct elements are:", result)

    result1 = slidingWindow(nums, window)
    print("The count of distinct elements using sliding window are:", result1)
