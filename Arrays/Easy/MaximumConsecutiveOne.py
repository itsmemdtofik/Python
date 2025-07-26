"""
 * <pre>
 * !Maximum Consecutive one's or zero in binary array.
 * Given a binary array, find the count of a maximum number of consecutive 1s
 * present in the array.
 *
 * Examples :
 * Input: arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
 * Output: 4
 * Explanation: The maximum number of consecutive 1’s in the array is 4 from
 * index 8-11.
 *
 * Input: arr[] = {0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1}
 * Output: 1
 * Explanation: The maximum number of consecutive 0’s in the array is 1 from
 * index 0-1.
 * </pre>
"""


def maximumConsecutiveOne(nums):
    if nums is None or len(nums) == 0:
        return 1
    countOne = 0
    for num in nums:
        if num == 1:
            countOne += 1
        else:
            countOne = 0
    return countOne


values = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
print(f"Maximum Consecutive One is: {maximumConsecutiveOne(values)}")
