def reverseNumber(number: int):
    reverse = 0
    while number != 0:
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = number // 10
    return reverse


print(reverseNumber(12345))
