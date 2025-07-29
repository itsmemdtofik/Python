"""
    /**
     * <pre>
     * !Subarray with given sum
     * Given a 1-based indexing array arr[] of non-negative integers and an integer sum.
     * You mainly need to return the left and right indexes(1-based indexing) of that subarray.
     *
     * Input: arr[] = [15, 2, 4, 8, 9, 5, 10, 23], target = 23
     * Output: [2, 5]
     * Explanation: Sum of subarray arr[2...5] is 2 + 4 + 8 + 9 = 23.
     * </pre>
"""


def subarrayWithGivenSum(nums: list[int], target: int) -> list[int]:
    result = []
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == target:
                result.append(i + 1)  # 1-based indexing
                result.append(j + 1)
                return result
    result.append(-1)
    return result


def slidingWindow(nums: list[int], target: int) -> list[int]:
    left = right = 0
    result = []
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum >= target:
            right = i

            while current_sum > target and left < right:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                result.append(left + 1)  # 1-based indexing
                result.append(right + 1)
                return result

    result.append(-1)
    return result


def main():
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23

    print("Using Brute-force O(n^2):")
    result1 = subarrayWithGivenSum(arr, target)
    print(" ".join(map(str, result1)))

    print("Using Sliding Window O(n):")
    result2 = slidingWindow(arr, target)
    print(" ".join(map(str, result2)))


if __name__ == "__main__":
    main()
