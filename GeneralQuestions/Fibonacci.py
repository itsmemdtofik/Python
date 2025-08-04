def getFibonacci(nums: int):
    a, b = 0, 1

    for _ in range(nums):
        print(a, end=" ")
        a, b = b, a + b  # Simultaneous update


if __name__ == '__main__':
    getFibonacci(10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
