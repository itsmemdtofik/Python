import math


def is_prime(num):
    """Check if a number is prime using trial division."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


n = 17
print(f"This is prime number: {is_prime(n)}")
