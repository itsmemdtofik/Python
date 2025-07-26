"""
 * <pre>
 * !Missing and repeating in an array.
 * Given an unsorted array of size n. Array elements are in the range of 1 to n.
 * One number from set {1, 2, …n} is missing and one number occurs twice in the
 * array. Find these two numbers.
 *
 * Examples:
 *
 * Input: arr[] = {3, 1, 3}
 * Output: Missing = 2, Repeating = 3
 * Explanation: In the array, 2 is missing and 3 occurs twice
 *
 *
 * Input: arr[] = {4, 3, 6, 2, 1, 1}
 * Output: Missing = 5, Repeating = 1
 * </pre>

"""


def missingAndRepeating(nums):
    if nums is None or len(nums) < 2:
        return nums

    seen = set()
    repeating = -1

    for num in nums:
        if num in seen:
            repeating = num
        else:
            seen.add(num)
    missing = -1
    for num in range(1, len(nums) + 1):
        if num not in seen:
            missing = num
            break
    return [missing, repeating]


arr = [1, 3, 3, 4, 5]
print(f"Missing and Repeating: {missingAndRepeating(arr)}")
