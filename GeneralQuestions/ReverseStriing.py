def getReverseStringUsingTwoPointer(s: str) -> str:
    # Convert String to list of characters
    chars = list(s)
    left = 0
    right = len(chars) - 1

    # Swap characters from both ends
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    # Convert back to string
    return ''.join(chars)


print(f"Using Pointer:")
print(getReverseStringUsingTwoPointer("hello"))  # "olleh"
print(getReverseStringUsingTwoPointer("Python"))  # "nohtyP"
print(getReverseStringUsingTwoPointer("racecar"))  # "racecar" (palindrome)
print(getReverseStringUsingTwoPointer(""))  # "" (edge case)


def getReverseStringUsingLoop(s: str) -> str:
    reversed = ""
    for i in range(len(s) - 1, -1, -1):
        reversed += s[i]
    return reversed


def getReverseStringUsingSlice(s: str) -> str:
    return s[::-1]


print(f"Using Slicing:")
print(getReverseStringUsingSlice("hello"))  # "olleh"
print(getReverseStringUsingSlice("Python"))  # "nohtyP"
print(getReverseStringUsingSlice("racecar"))  # "racecar" (palindrome)
print(getReverseStringUsingSlice(""))  # "" (edge case)
