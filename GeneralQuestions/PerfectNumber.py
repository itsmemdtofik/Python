def getPerfectNumber(number:int) -> bool:

    sum = 0
    for num in range(1, number):
        if number % num == 0:
            sum += num
    return sum == number



print(getPerfectNumber(15))
print(getPerfectNumber(16))
print(getPerfectNumber(100))
print(getPerfectNumber(10000))