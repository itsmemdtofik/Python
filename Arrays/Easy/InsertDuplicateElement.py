"""
 * <pre>
 * !Insert duplicate of K adjacent to it for its every occurrences in array.
 *
 * Given an array arr consisting of N integers and an integer K, the task is to
 * insert an adjacent K for every occurrence of it in the original sequence and
 * then truncate the array to the original length using an O(1) auxiliary space.
 *
 * Examples:
 *
 * Input: arr[] = {1, 0, 2, 3, 0, 4, 5, 0}, K = 0
 * Output: {1, 0, 0, 2, 3, 0, 0, 4}
 * Explanation:
 * The given array {1, 0, 2, 3, 0, 4, 5, 0} is modified to {1, 0, 0, 2, 3, 0, 0, 4]
 * after insertion of two 0’s and truncation of extra elements.
 *
 *
 * Input: arr[] = {7, 5, 8}, K = 8
 * Output: {7, 5, 8}
 * Explanation:
 * After inserting an adjacent 8 into the array, it got truncated to restore the
 * original size of the array.
 * !Approach: Time complexity: O(n), Space complexity: O(n)
 * Step1: First we counted all the K in arr
 * Step2: And we created a new arr ith length of newArr = [arr.length + count] and stored all items into it and truncated it.
 * Step3: Return new array
 * </pre>
"""


def insertDuplicate(nums, K):
    if nums is None or len(nums) < 2:
        return nums

    # Count occurrences of K
    count = sum(1 for num in nums if num == K)

    # Create new list with increased size
    new_array = [0] * (len(nums) + count)

    j = 0
    for num in nums:
        new_array[j] = num
        j += 1

        if num == K:
            new_array[j] = K
            j += 1
    return new_array


arr = [1, 2, 3, 2, 4]
K = 2
result = insertDuplicate(arr, K)
print(f"Array after inserting duplicate of {K}: {result}")
