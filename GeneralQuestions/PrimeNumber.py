import math


def getPrime(number: int) -> bool:
    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for num in range(3, int(math.sqrt(number)) + 1, 2):
        if number % num == 0:
            return False
    return True


print(getPrime(2))  # True
print(getPrime(17))  # True
print(getPrime(100))  # False
print(getPrime(1))  # False


# Even More Optimized Version (6k ± 1 optimization):
def getPrimeII(number: int) -> bool:
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
        w = 6 - w
    return True


print(getPrimeII(2))  # True
print(getPrimeII(17))  # True
print(getPrimeII(100))  # False
print(getPrimeII(1))  # False
