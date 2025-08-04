def getAnagramCheckUsingBubbleSort(s1: str, s2: str) -> bool:
    # Convert string to list
    a = list(s1)
    b = list(s2)

    # Apply bubble sort now
    def sortCharacter(chars):
        n = len(chars)

        for i in range(n):
            for j in range(0, n - i - 1):
                if chars[j] > chars[j + 1]:
                    chars[j], chars[j + 1] = chars[j + 1], chars[j]
        return chars

    # Sort Both Lists
    a_sorted = sortCharacter(a)
    b_sorted = sortCharacter(b)

    # Compare character by character
    if len(a_sorted) != len(b_sorted):
        return False

    for i in range(len(a_sorted)):
        if a_sorted[i] != b_sorted[i]:
            return False
    return True


print(f"Using Bubble Sort: ")
print(getAnagramCheckUsingBubbleSort("listen", "silent"))  # True
print(getAnagramCheckUsingBubbleSort("hello", "world"))  # False
print(getAnagramCheckUsingBubbleSort("anagram", "nagaram"))  # True
print(getAnagramCheckUsingBubbleSort("rat", "car"))  # False


def getAnagramStringCheck(s1: str, s2: str) -> bool:
    sorted_string1 = sorted(s1)
    sorted_string2 = sorted(s2)

    return sorted_string1 == sorted_string2


print(f"Using sorted: ")
print(getAnagramStringCheck("listen", "silent"))  # True
print(getAnagramStringCheck("hello", "world"))  # False
print(getAnagramStringCheck("anagram", "nagaram"))  # True
print(getAnagramStringCheck("rat", "car"))  # False


def getAnagramStringCheckUsingHashMap(s1: str, s2: str) -> bool:
    from collections import defaultdict
    if len(s1) != len(s2):
        return False

    # Count character manually here
    freq_map1 = defaultdict(int)
    freq_map2 = defaultdict(int)

    for char in s1:
        freq_map1[char] = freq_map1[char] + 1

    for char in s2:
        freq_map2[char] = freq_map2[char] + 1

    return freq_map1 == freq_map2


print(f"Using HashMap: ")
print(getAnagramStringCheckUsingHashMap("listen", "silent"))  # True
print(getAnagramStringCheckUsingHashMap("hello", "world"))  # False
print(getAnagramStringCheckUsingHashMap("anagram", "nagaram"))  # True
print(getAnagramStringCheckUsingHashMap("rat", "car"))  # False


def getAnagramStringCheckUsingHashMapII(s1: str, s2: str) -> bool:
    from collections import defaultdict
    if len(s1) != len(s2):
        return False

    # Count character manually here
    freq_map1 = defaultdict(int)
    freq_map2 = defaultdict(int)

    for char in s1:
        freq_map1[char] = freq_map1.get(char, 0) + 1

    for char in s2:
        freq_map2[char] = freq_map2.get(char, 0) + 1

    return freq_map1 == freq_map2


print(f"Using HashMap in Another Approach: ")
print(getAnagramStringCheckUsingHashMapII("listen", "silent"))  # True
print(getAnagramStringCheckUsingHashMapII("hello", "world"))  # False
print(getAnagramStringCheckUsingHashMapII("anagram", "nagaram"))  # True
print(getAnagramStringCheckUsingHashMapII("rat", "car"))  # False
