"""
 * <pre>
 * !Move all zeros to end of an array.
 * Given an array of integers arr[], the task is to move all the zeros to
 * the end of the array while maintaining the relative order of all non-zero elements.
 *
 * Examples:
 * Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0
 * Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0
 * Explanation: There are three 0s that are moved to the end.
 *
 * Input: arr[] = [10, 20, 30]
 * Output: arr[] = [10, 20, 30]
 * Explanation: No change in array as there are no 0s.
 *
 * Input: arr[] = [0, 0]
 * Output: arr[] = [0, 0]
 * Explanation: No change in array as there are all 0s.
 * </pre>

"""


def moveZerosToEndUsingList(nums):
    if nums is None:
        return None

    result: list = []
    count = 0

    for num in nums:
        if num == 0:
            count += 1
        else:
            result.append(num)

    for _ in range(count):
        result.append(0)

    return result


arr = [1, 0, 1, 0, 3, 0, 10, 0, 20, 0, 12]
print("After moving zeros to end:", moveZerosToEndUsingList(arr))
