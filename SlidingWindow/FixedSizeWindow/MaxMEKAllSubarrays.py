"""
	 * <pre>
	 * !Maximum MEX(Minimum Excluded Value) from all subarrays of length K
	 * Given an array arr[] consisting of N distinct integers and an integer K,
	 * the task is to find the maximum MEX from all subarrays of length K.
	 *
	 * Input: arr[] = {3, 2, 1, 4}, K = 2
	 * Output: 3
	 * Explanation:
	 * All subarrays having length 2 are {3, 2}, {2, 1}, {1, 4}.
	 * In subarray {3, 2}, the smallest positive integer which is not present is 1.
	 * In subarray {2, 1}, the smallest positive integer which is not present is 3.
	 * In subarray {1, 4}, the smallest positive integer which is not present is 2.
	 * </pre>

"""


def computeMEX(seen: set[int]):
    mex = 1
    while mex in seen:
        mex += 1
    return mex


def MaxMEXSubarray(nums: int, window: int):
    max_mex = 0
    result = []
    seen = set()

    for i in range(window):
        seen.add(nums[i])

    mex = computeMEX(seen)
    max_mex = max(max_mex, mex)

    for i in range(window, len(nums)):
        seen.discard(nums[i - window])  # remove leftmost element
        seen.add(nums[i])  # add new element
        mex = computeMEX(seen)
        max_mex = max(max_mex, mex)

    result.append(max_mex)
    return result


if __name__ == "__main__":
    nums = [3, 1, 2, 4]
    window = 2
    result = MaxMEXSubarray(nums, window)
    print("All are:", result)

    nums1 = [6, 1, 3, 2, 4]
    window1 = 3
    result1 = MaxMEXSubarray(nums1, window1)
    print("All are:", result1)
