def getDecimalToBinary(decimal: int) -> str:
    if decimal == 0:
        return "0"

    binary = []
    num = abs(decimal)  # To handle negative number

    while num > 0:
        remainder = str(num % 2)
        binary.append(remainder)
        num = num // 2

    # Reversed to get correct order
    binary_str = ''.join(reversed(binary))

    return binary_str if decimal >= 0 else "-" + binary_str


print("Using Division Method")
print(getDecimalToBinary(10))  # "1010"
print(getDecimalToBinary(15))  # "1111"
print(getDecimalToBinary(0))  # "0"
print(getDecimalToBinary(1))  # "1"
print(getDecimalToBinary(-5))  # "-101"


def getDecimalToBinaryUsingBitShifting(decimal: int) -> str:
    if decimal == 0:
        return "0"

    binary = []
    num = abs(decimal)

    while num > 0:
        binary.append(str(num & 1))  # Get the least significant bit
        num >>= 1  # Right shift (equivalent to // 2)

    binary_str = ''.join(reversed(binary))
    return binary_str if decimal >= 0 else "-" + binary_str


print("getDecimalToBinaryUsingBitShifting: ")
print(getDecimalToBinaryUsingBitShifting(10))  # "1010"
print(getDecimalToBinaryUsingBitShifting(15))  # "1111"
print(getDecimalToBinaryUsingBitShifting(0))  # "0"
print(getDecimalToBinaryUsingBitShifting(1))  # "1"
print(getDecimalToBinaryUsingBitShifting(-5))  # "-101"
