"""
 * <pre>
 * ! Minimize Height
 *
 * Given an array arr[] denoting heights of N towers and a positive integer K.
 *
 * For each tower, you must perform exactly one of the following operations
 * exactly once.
 *
 * Increase the height of the tower by K
 * Decrease the height of the tower by K
 * Find out the minimum possible difference between the height of the shortest
 * and tallest towers after you have modified each tower.
 *
 * You can find a slight modification of the problem here.
 * Note: It is compulsory to increase or decrease the height by K for each
 * tower. After the operation, the resultant array should not contain any
 * negative integers.
 *
 * Examples :
 *
 * Input: k = 2, arr[] = {1, 5, 8, 10}
 * Output: 5
 * Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6,
 * 8}.The difference between the largest and the smallest is 8-3 = 5.
 *
 * Input: k = 3, arr[] = {3, 9, 12, 16, 20}
 * Output: 11
 * Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6,
 * 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11.
 * </pre>

"""


def minimizeHeight(nums: list, k: int):
    if not nums or len(nums) <= 0:
        return -1

    nums.sort()
    n = len(nums)

    initialDifference = nums[-1] - nums[0]
    minHeighSoFar = nums[0] + k
    maxHeightSoFar = nums[-1] - k

    for num in range(n - 1):
        current = nums[num]
        nextValue = nums[num + 1]

        possibleMin = min(minHeighSoFar, nextValue - k)
        possibleMax = max(maxHeightSoFar, current + k)

        if possibleMin < 0:
            continue  # Height can not be negative

        initialDifference = min(initialDifference, possibleMax - possibleMin)

    return initialDifference


arr1 = [1, 5, 8, 10]
print(minimizeHeight(arr1, 2))  # Expected Output: 5

arr2 = [3, 9, 12, 16, 20]
print(minimizeHeight(arr2, 3))  # Expected Output: 11
