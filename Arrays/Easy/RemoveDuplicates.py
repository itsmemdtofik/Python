"""
 * <pre>
 * !Remove duplicate from sorted array.
 *
 * Given a sorted array arr[] of size n, the goal is to rearrange the array so
 * that all distinct elements appear at the beginning in sorted order
 * Additionally, return the length of this distinct sorted subarray.
 * Note: The elements after the distinct ones can be in any order and hold any
 * value, as they don’t affect the result.
 *
 * Examples:
 * Input: arr[] = [2, 2, 2, 2, 2
 * Output: [2
 * Explanation: All the elements are 2, So only keep one instance of 2.
 *
 * Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5,
 * Output: [1, 2, 3, 4, 5
 * Input: arr[] = [1, 2,
 * Output: [1, 2,
 * Explanation : No change as all elements are distinct.
 * </pre>
"""


def removeDuplicates(nums):
    if nums is None or len(nums) < 2:
        return nums

    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


def duplicateRemoval(nums):
    if nums is None or len(nums) < 2:
        return nums

    result = [nums[0]]  # Always include the first element

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            result.append(nums[i])

    return result


arr = [1, 1, 2, 2, 3, 4, 4]
new_length = removeDuplicates(arr)
print(f"Original: {arr}")
print(f"Length after removing duplicates: {new_length}")
print(f"Array after removing duplicates: {arr[:new_length]}")

arr1 = [1, 1, 2, 2, 3, 4, 4]
unique_arr = duplicateRemoval(arr1)
print(f"Original: {arr1}")
print(f"Without duplicates: {unique_arr}")
