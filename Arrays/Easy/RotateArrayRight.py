"""
 * <pre>
 * !Rotate array by D positions to the right (clockwise).
 *
 * Given an array of integers arr[] of size n, the task is to rotate the array
 * elements to the right by d positions.
 *
 * Examples:
 *
 * Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
 * Output: {5, 6, 1, 2, 3, 4}
 * Explanation:
 * After first right rotation:  {6, 1, 2, 3, 4, 5}
 * After second right rotation: {5, 6, 1, 2, 3, 4}
 *
 * Input: arr[] = {1, 2, 3}, d = 4
 * Output: {3, 1, 2}
 * Explanation:
 * After one right rotation:   {3, 1, 2}
 * After two right rotations:  {2, 3, 1}
 * After three right rotations:{1, 2, 3}
 * After four right rotations: {3, 1, 2}
 * </pre>
"""


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotateArrayRight(nums, d):
    if len(nums) < 1:
        return nums

    d = d % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, d - 1)
    reverse(nums, d, len(nums) - 1)

    return nums


arr: list[int] = [1, 2, 3, 4, 5, 6]
position = 2
print("Rotated Array:", rotateArrayRight(arr, position))
