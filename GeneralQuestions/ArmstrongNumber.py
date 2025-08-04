def getArmstrongNumber(number: int) -> bool:
    if number < 0:
        return False

    temp = number
    digits = len(str(number))
    sum = 0

    while temp != 0:
        remainder = temp % 10
        sum = sum + remainder ** digits  # Python's exponentiation operator
        temp = temp // 10

    return sum == number


print(getArmstrongNumber(153))  # True (1³ + 5³ + 3³ = 153)
print(getArmstrongNumber(9474))  # True (9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474)
print(getArmstrongNumber(123))  # False
print(getArmstrongNumber(-153))  # False
