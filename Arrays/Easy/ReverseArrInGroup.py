"""
 * <pre>
 * !Reverse an Array in groups of given size.
 * Given an array arr[] and an integer K, the task is to reverse every
 * subarray formed by consecutive K elements.
 * Examples:
 * Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9], K = 3
 * Output: 3, 2, 1, 6, 5, 4, 9, 8, 7
 *
 * Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], K = 5
 * Output: 5, 4, 3, 2, 1, 8, 7, 6
 *
 * Input: arr[] = [1, 2, 3, 4, 5, 6], K = 1
 * Output: 1, 2, 3, 4, 5, 6
 *
 * Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], K = 10
 * Output: 8, 7, 6, 5, 4, 3, 2, 1
 * </pre>
"""


def reverseArrayInGroup(nums, k):
    if nums is None or len(nums) < 3:
        return nums

    for start in range(0, len(nums), k):
        left = start
        right = min(start + k - 1, len(nums) - 1)

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K: int = 3
print("Reversed in groups:", reverseArrayInGroup(arr, K))
