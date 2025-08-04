def getBinaryToDecimal(binary_str: str) -> int:
    decimal = 0
    length = len(binary_str)

    for i in range(length):
        # Get the current bit (starting from left / MSB)
        bit = int(binary_str[i])

        # Calculate power of 2 (2 ^ (position from right))
        power = length - i - 1

        # Add to the result
        decimal = decimal + bit * (2 ** power)
    return decimal


def getBinaryToDecimalUsingBitShifting(binary_str: str) -> int:
    decimal = 0
    for bit in binary_str:
        decimal = (decimal << 1) | int(bit)
    return decimal


if __name__ == '__main__':
    print(getBinaryToDecimalUsingBitShifting("1010"))  # 10
    print(getBinaryToDecimalUsingBitShifting("1111"))  # 15
    print(getBinaryToDecimalUsingBitShifting("10000"))  # 16
    print(getBinaryToDecimalUsingBitShifting("1"))  # 1 (edge case)
    print(getBinaryToDecimalUsingBitShifting("0"))  # 0 (edge case)
