"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""


def merge(nums1: list, nums2: list) -> list:
    i = j = mergedIdx = 0
    merged = [0] * (len(nums1) + len(nums2))

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:  # Simplified condition
            merged[mergedIdx] = nums1[i]
            i += 1
        else:
            merged[mergedIdx] = nums2[j]  # Fixed: Use nums2[j]
            j += 1
        mergedIdx += 1

    # Append remaining elements
    while i < len(nums1):
        merged[mergedIdx] = nums1[i]
        i += 1
        mergedIdx += 1

    while j < len(nums2):
        merged[mergedIdx] = nums2[j]
        j += 1
        mergedIdx += 1

    return merged


def median(nums1: list, nums2: list) -> float:
    merged = merge(nums1, nums2)
    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2  # Correct average


if __name__ == "__main__":
    arr1 = [1, 2, 2]
    arr2 = [3, 4, 4]

    median1 = median(arr1, arr2)
    print(f"The median is: {median1}")

    arr3 = [1, 2]
    arr4 = [3, 4, 5]
    median2 = median(arr3, arr4)
    print(f"Median is: {median2}")
