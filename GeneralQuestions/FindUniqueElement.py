from collections import defaultdict


def getUniqueElementUsingHashMap(arr: list[int]) -> dict | None:
    freq = defaultdict(int)

    # Count occurrences of each number
    for num in arr:
        freq[num] += 1

    # Find the number with count 1
    for num, count in freq.items():
        if count == 1:
            return num

    return None  # If no single element found (though problem states one exists)


print(f"Unique Element Using HashMap:")
print(getUniqueElementUsingHashMap([2, 3, 4, 2, 3]))  # 4
print(getUniqueElementUsingHashMap([1, 1, 2, 2, 3]))  # 3
print(getUniqueElementUsingHashMap([7]))  # 7
print(getUniqueElementUsingHashMap([4, 1, 2, 1, 2]))  # 4
print(getUniqueElementUsingHashMap([-1, -1, -2]))  # -2


def getUniqueElementUsingXOR(arr: list[int]) -> int:
    result = 0
    for num in arr:
        result ^= num
    return result


print(f"Unique Element using XOR: ")
print(getUniqueElementUsingXOR([2, 3, 4, 2, 3]))  # 4
print(getUniqueElementUsingXOR([1, 1, 2, 2, 3]))  # 3
print(getUniqueElementUsingXOR([7]))  # 7 (edge case)
print(getUniqueElementUsingXOR([4, 1, 2, 1, 2]))  # 4
print(getUniqueElementUsingXOR([-1, -1, -2]))  # -2 (works with negatives)
