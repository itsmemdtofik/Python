from PrimeNumber import getPrime, getPrimeII


def getAllPrimeNumbers(number: int) -> list[int]:
    primes = []
    for num in range(2, number + 1):
        if getPrimeII(num):
            primes.append(num)
    return primes


print(getAllPrimeNumbers(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(getAllPrimeNumbers(100))  # All primes ≤ 100
