def AddOneUsingStack(number):
    if len(number) == 0:
        return number

    stack = []
    carry = 1
    n = len(number) - 1

    while n >= 0 or carry > 0:
        digit = number[n] + carry if n >= 0 else carry
        stack.append(digit % 10)
        carry = digit // 10
        n = n - 1
    result = []
    while stack:
        result.append(stack.pop())
    return result


print("Using the Stack")
print(AddOneUsingStack([1, 2, 3]))  # Output: [1, 2, 4]
print(AddOneUsingStack([9, 9, 9]))  # Output: [1, 0, 0, 0]
print(AddOneUsingStack([]))  # Output: []
