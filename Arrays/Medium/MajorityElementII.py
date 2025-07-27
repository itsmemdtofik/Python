"""
     * <pre>
     * ! Majority Element II - An element that occure [arr.length / 3] times.
     *
     * Given an array arr[] consisting of n integers, the task is to find all the
     * array elements which occurs more than floor(n/3) times.
     * Note: The returned array of majority elements should be sorted.
     *
     * Examples:
     *
     * Input: arr[] = {2, 2, 3, 1, 3, 2, 1, 1}
     * Output: {1, 2}
     * Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3
     * = 2).
     *
     *
     * Input: arr[] = {-5, 3, -5}
     * Output: {-5}
     * Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 =
     * 1).
     *
     *
     * Input: arr[] = {3, 2, 2, 4, 1, 4}
     * Output: { }
     * Explanation: There is no majority element.
     * </pre>

"""


def majorityElementII(nums: list):
    if len(nums) < 0 or nums is None:
        return []

    hashMap = {}
    result = []

    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1

    for num, count in hashMap.items():
        if count > len(nums) // 3:
            result.append(num)
    return result


if __name__ == "__main__":
    arr1 = [3, 2, 3]
    print("Expected: [3] == ", majorityElementII(arr1))

    arr2 = [1, 1, 1, 3, 3, 2, 2, 2]
    print("Expected: [1, 2] == ", majorityElementII(arr2))

    arr3 = []
    print("Expected: [] == ", majorityElementII(arr3))
