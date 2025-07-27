"""
     * <pre>
     * !Maximum Product Subarray
     * Given an integer array, the task is to find the maximum product of any subarray.
     *
     * Input: arr[] = {-2, 6, -3, -10, 0, 2}
     * Output: 180
     * Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180
     *
     * Input: arr[] = {-1, -3, -10, 0, 60}
     * Output: 60
     * Explanation: The subarray with maximum product is {60}.
     *
     * !Approach: By using Kadane’s algorithm – O(n) Time and O(1) Space
     *
     * </pre>

"""


def maximumProductOfSubarrayUsingNestedLoop(nums: list[int]):
    if nums is None or len(nums) == 0:
        raise ValueError("Array must not be empty or null")

    max_product = float('-inf')
    n = len(nums)

    for start in range(n):
        current_product = 1
        for end in range(start, n):
            current_product *= arr[end]
            max_product = max(max_product, current_product)

    return max_product


def maximumProductOfSubarray(nums: list):
    if nums is None or len(nums) == 0:
        raise ValueError("Array must not be null or empty!")

    maxProduct = minProduct = maxGlobal = nums[0]

    for num in range(1, len(nums)):
        if nums[num] < 0:
            maxProduct, minProduct = minProduct, maxProduct

        maxProduct = max(maxProduct * nums[num], nums[num])
        minProduct = min(minProduct * nums[num], nums[num])

        maxGlobal = max(maxGlobal, maxProduct)

    return maxGlobal


if __name__ == "__main__":
    arr_list = [
        [-2, 6, -3, -10, 0, 2],
        [-1, -3, -10, 0, 60],
        [2, 3, -2, 4],
        [-2, 0, -1]
    ]

    for i, arr in enumerate(arr_list, 1):
        print(f"Array {i}: {arr}")
        print(f"Maximum product: {maximumProductOfSubarrayUsingNestedLoop(arr)}\n")
