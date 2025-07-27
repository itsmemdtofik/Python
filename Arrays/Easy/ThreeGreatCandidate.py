"""
 * <pre>
 * !Maximum product of a triplet (subsequence of size 3) in array.
 * !Approach
 * Step1: Find first and second and third largest element.
 * Step2: Return of first * second * third.
 * Given an integer array, find a maximum product of a triplet in the array.
 *
 * Examples:
 * Input:  [10, 3, 5, 6, 20]
 * Output: 1200
 * Explanation: Multiplication of 10, 6 and 20
 *
 * Input:  [-10, -3, -5, -6, -20]
 * Output: -90
 *
 * Input:  [1, -4, 3, -6, 7, 0]
 * Output: 168
 * </pre>
"""


def productOfTriplet(nums):
    if len(nums) < 3:
        return 0

    first = second = third = float('-inf')
    minimumOne = minimumSecond = float('inf')

    for num in nums:

        if num > first:
            third, second, first = second, first, num
        elif num > second:
            third, second = second, num
        elif num > third:
            third = num
        # Update the two smallest numbers
        if num < minimumOne:
            minimumSecond, minimumOne = minimumOne, num
        elif num < minimumSecond:
            minimumSecond = num
    # Compare the two possible cases
    return max(first * second * third, minimumOne * minimumSecond * first)


if __name__ == "__main__":
    print(productOfTriplet([1, 2, 3, 4]))  # Output: 24 (4*3*2)
    print(productOfTriplet([-10, -5, 0, 1, 2]))  # Output: 100 (-10*-5*2)
    print(productOfTriplet([5, 5, 5]))  # Output: 125 (5*5*5)
    print(productOfTriplet([1, 2]))  # Output: 0 (edge case)
