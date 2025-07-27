"""
 * <pre>
 * !Rotate array by D positions to the left (counter-clockwise).
 *
 * Given an array of integers arr[] of size n, the task is to rotate the array
 * elements to the left by d positions.
 *
 * Examples:
 *
 * Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
 * Output: {3, 4, 5, 6, 1, 2}
 * Explanation:
 * After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1}
 * After the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}
 *
 * Input: arr[] = {1, 2, 3}, d = 4
 * Output: {2, 3, 1}
 * Explanation:
 * After first left rotation, arr[] = {2, 3, 1}
 * After second left rotation, arr[] = {3, 1, 2}
 * After third left rotation, arr[] = {1, 2, 3}
 * After fourth left rotation, arr[] = {2, 3, 1}
 * </pre>
"""


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotateArrayLeft(nums, d):
    if len(nums) < 1:
        return nums

    d = d % len(nums)
    reverse(nums, 0, d - 1)
    reverse(nums, d, len(nums) - 1)
    reverse(nums, 0, len(nums) - 1)

    return nums


arr: list[int] = [1, 2, 3, 4, 5, 6]
position = 2
print("Rotated Array:", rotateArrayLeft(arr, position))
