"""
     * <pre>
     * !Ways to make sum of odd and even indexed elements equal by removing an array element
     * Given an array, arr[] of size n, the task is to find the count of array indices
     * such that removing an element from these indices makes the sum of even-indexed
     * and odd-indexed array elements equal.
     *
     * @param Examples:
     * Input: arr[] = [ 2, 1, 6, 4 ]
     * Output: 1
     * Explanation: Removing arr[1] from the array modifies arr[] to [ 2, 6, 4 ] such that, arr[0] + arr[2] = arr[1].
     * Therefore, the required output is 1.
     *
     * Input: arr[] = [ 1, 1, 1 ]
     * Output: 3
     * Explanation: Removing arr[0] from the given array modifies arr[] to [ 1, 1 ] such that arr[1] = arr[2]
     * Removing arr[1] from the given array modifies arr[] to [ 1, 1 ] such that arr[0] = arr[2]
     * Removing arr[2] from the given array modifies arr[] to [ 1, 1 ] such that arr[0] = arr[1]
     * Therefore, the required output is 3.
     *
     * !Approach: Using Nested Loop – O(n^2) Time and O(1) Space
     * The simplest approach to solve this problem is to traverse the array and for each array element,
     * check if removing the element from the array makes the sum of even-indexed and odd-indexed array elements equal or not.
     * If found to be true, then increment the count. Finally, print the count.
     * </pre>
"""


def minimumIndicesToEqualEvenOdd(nums: list) -> list[int]:
    n = len(nums)
    count = 0

    for i in range(n):

        evenSum = oddSum = k = 0
        for j in range(n):

            if j == i:
                continue
            if k % 2 == 0:
                evenSum += nums[j]
            else:
                oddSum += nums[j]
            k += 1
        if evenSum == oddSum:
            count += 1
    return count


nums1 = [2, 1, 6, 4]
nums2 = [1, 1, 1]

print(f"Minimum Height is : {minimumIndicesToEqualEvenOdd(nums1)}")

print(f"Minimum Height is : {minimumIndicesToEqualEvenOdd(nums2)}")
