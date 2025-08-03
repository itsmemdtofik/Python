def getSumOfDigits(nums: int) -> int:
    num = abs(nums)  # Handle negative numbers by taking absolute value
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num = num // 10
    return sum_digits


print(getSumOfDigits(12345))
