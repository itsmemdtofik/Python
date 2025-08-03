def reverseNumber(num: int) -> int:
    reversedNumber = 0
    number = abs(num)
    while abs(number) != 0:
        remainder = number % 10
        reversedNumber = reversedNumber * 10 + remainder
        number = number // 10
    return reversedNumber


def isPalindromeNumber(number: int) -> bool:
    if number < 0:
        return False  # Negative can not be palindrome
    return number == reverseNumber(number)


print(isPalindromeNumber(12321))  # True
print(isPalindromeNumber(12345))  # False
print(isPalindromeNumber(-121))  # False
