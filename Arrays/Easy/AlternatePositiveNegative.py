"""
 * !Rearrange element by sign
 * !Time complexity: O(n), Space complexity: O(n)
 * Given an array arr[] of size n, the task is to rearrange it in alternate
 * positive and negative manner without changing the relative order of positive
 * and negative numbers. In case of extra positive/negative numbers, they appear
 * at the end of the array.
 *
 * Note: The rearranged array should start with a positive number and 0 (zero)
 * should be considered as a positive number.
 *
 * Examples:
 *
 * Input: arr[] = {1, 2, 3, -4, -1, 4}
 * Output: arr[] = {1, -4, 2, -1, 3, 4}
 *
 *
 * Input: arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
 * Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
 *
 * !Approach: There is two solution for this Stack and List
 * Step1: Create two list one for non-negative and one for negative.
 * Step2: Merge the positive and Negative list alternatively.
 * Step3: Handle remaining Positive and Negative Number.
 * Step4: Convert list back into an array.
 * Step5: Return the array
"""


def UsingList(nums):
    if not nums or len(nums) < 2:
        return nums

    positive_list = []
    negative_list = []

    for num in nums:
        if num >= 0:
            positive_list.append(num)
        else:
            negative_list.append(num)

    merged_list = []
    i = j = 0

    # Merge alternating elements
    while i < len(positive_list) and j < len(negative_list):
        merged_list.append(positive_list[i])
        merged_list.append(negative_list[j])
        i += 1
        j += 1

    # Add remaining positives
    while i < len(positive_list):
        merged_list.append(positive_list[i])
        i += 1

    # Add remaining negatives
    while j < len(negative_list):
        merged_list.append(negative_list[i])
        j += 1

    return merged_list


print(UsingList([3, -2, 5, -7, 6, -1]))
# Output: [3, -2, 5, -7, 6, -1]

print(UsingList([-4, -3, 1, 2, 3]))
# Output: [1, -4, 2, -3, 3]
