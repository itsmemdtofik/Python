"""
 * <pre>
 * !Finding some of the digits of a number until sum become single digit.
 *
 * Given an integer n, we need to repeatedly find the sum of its digits until
 * the result becomes a single-digit number.
 *
 * Examples:
 *
 * Input: n = 1234
 * Output: 1
 * Explanation:
 * Step 1: 1 + 2 + 3 + 4 = 10
 * Step 2: 1 + 0 = 1
 *
 *
 * Input: n = 5674
 * Output: 4
 * Explanation:
 * Step 1: 5 + 6 + 7 + 4 = 22
 * Step 2: 2 + 2 = 4
 * </pre>
"""


def findSumOfDigits(nums):
    if nums is None or len(nums) == 0:
        return nums

    sumArray = 0
    sumDigit = 0

    for num in nums:
        sumArray = sumArray + num

    while sumArray != 0:
        rem = sumArray % 10
        sumDigit = sumDigit + rem
        sumArray = sumArray // 10

    return sumDigit


arr = [123, 456]
print(findSumOfDigits(arr))  # Output: 1 + 2 + 3 + 4 + 5 + 6 = 21


def sumToSingleDigit(number: int):
    if number < 0:
        raise ValueError("The number must be greater than zero!")

    while number >= 10:
        sumOfDigit = 0
        while number > 0:
            rem: int = number % 10
            sumOfDigit += rem
            number //= 10
        number = sumOfDigit
    return number


print(sumToSingleDigit(1234))  # Output: 1
print(sumToSingleDigit(5674))  # Output: 4
print(sumToSingleDigit(9))  # Output: 9
