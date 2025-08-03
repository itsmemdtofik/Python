def getFactorial(nums: int) -> int:
    if not isinstance(nums, int) or nums < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    fact: int = 1
    for num in range(2, nums + 1):
        fact *= num
    return fact


print(getFactorial(5))
