"""
     * <pre>
     * !Minimum number of decrement-other operations to make all array elements equal.
     * We are given an array consisting of n elements.
     * At each operation we can select any one element and increase rest of n-1 elements by 1.
     * We have to make all elements equal performing such operation as many times you wish.
     * Find the minimum number of operations needed for this.
     *
     * @param Examples:
     * Input: arr[] = [1, 2, 3]
     * Output: 2
     * Explanation:
     * Operation 1 : Decrement 3 (the max) by 1 -> [1, 2, 2]
     * Operation 2 : Decrement one of the 2's by 1 -> [1, 1, 2] or [1, 2, 1]
     * Operation 3 : Decrement the remaining 2 by 1 -> [1, 1, 1]
     *
     * </pre>
"""


def minimumMovesToEqualize(nums: list[int]) -> int:
    if not nums:
        return 0

    minimumNumber = min(nums)
    maximumNumber = max(nums)

    return maximumNumber - minimumNumber


nums1 = [1, 2, 3]
nums2 = [4, 3, 4]

print(f"Minimum Moves is: {minimumMovesToEqualize(nums1)}")
print(f"Minimum Moves is: {minimumMovesToEqualize(nums2)}")
