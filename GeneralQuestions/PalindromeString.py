def getPalindromeString(s: str) -> bool:
    return s == s[::-1]


# Palindrome Tests
print(f"Using Slicing:")
print(getPalindromeString("racecar"))  # True
print(getPalindromeString("hello"))  # False
print(getPalindromeString("A man a plan a canal Panama"))  # False (needs normalization)


def getPalindromeStringNormalization(s: str) -> bool:
    normalized = [c.lower() for c in s if c.isalnum()]
    return normalized == normalized[::-1]


# Palindrome Tests
print(f"using normalization")
print(getPalindromeStringNormalization("racecar"))  # True
print(getPalindromeStringNormalization("hello"))  # False
print(getPalindromeStringNormalization("A man a plan a canal Panama"))  # False (needs normalization)
