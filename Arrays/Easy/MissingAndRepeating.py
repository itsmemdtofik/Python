# ! Missing and Repeating in an array
# 
# Given an unsorted array of size n. Array elements are in the range of 1 to n.
# One number from set {1, 2, …n} is missing and one number occurs twice in the array.
# Find these two numbers.
#
# Examples:
# Input: arr = [3, 1, 3]
# Output: Missing = 2, Repeating = 3
#
# Input: arr = [4, 3, 6, 2, 1, 1]
# Output: Missing = 5, Repeating = 1


def missing_and_repeating(nums):
    """
    * Approach 1:
    Step1: Create a visited array of size n+1 initialized to False.
    Step2: Traverse the input array:
        - If visited[num] is False, set visited[num] = True
        - If visited[num] is already True, this is the repeating number.
    Step3: Traverse visited[] to find the missing number where visited[i] is still False.
    """
    visited = [False] * (len(nums) + 1)
    repeating = -1
    missing = -1

    for num in nums:
        if visited[num]:
            repeating = num
        else:
            visited[num] = True

    for i in range(1, len(nums) + 1):
        if not visited[i]:
            missing = i
            break

    print("Repeating:", repeating)
    print("Missing:", missing)


def find_missing_and_repeating(nums):
    """
    * Approach 2:
    Step1: Use a HashSet to track numbers.
    Step2: Iterate through array:
        - If number is already in the set, it is repeating.
        - Otherwise, add it to the set.
    Step3: Missing number is the one from 1 to n not present in the set.
    """
    if nums is None or len(nums) < 2:
        return nums

    num_set = set()
    repeating = -1

    for num in nums:
        if num in num_set:
            repeating = num
        else:
            num_set.add(num)

    missing = -1
    for i in range(1, len(nums) + 1):
        if i not in num_set:
            missing = i
            break

    return [missing, repeating]


if __name__ == "__main__":
    arr = [7, 3, 4, 5, 5, 6, 2]
    missing_and_repeating(arr)

    arr1 = [3, 1, 3]
    arr2 = [4, 3, 6, 2, 1, 1]

    result1 = find_missing_and_repeating(arr1)
    print("Missing =", result1[0], ", Repeating =", result1[1])

    result2 = find_missing_and_repeating(arr2)
    print("Missing =", result2[0], ", Repeating =", result2[1])
