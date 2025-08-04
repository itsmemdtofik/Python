def getGCD(a: int, b: int) -> int:
    if b == 0:
        return a

    return getGCD(b, a % b)


def getLCM(a: int, b: int) -> int:
    return (a * b) // getGCD(a, b)


print(getGCD(48, 18))  # 6
print(getGCD(0, 5))  # 5
print(getGCD(-15, 25))  # 5 (works with negatives)

print(getLCM(12, 15))  # 60
print(getLCM(0, 5))  # 0 (edge case)
print(getLCM(-4, 6))  # 12 (works with negatives)


# Iterative GCD (avoids recursion limits)
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)  # Ensure positive result


# LCM with edge case handling
def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
