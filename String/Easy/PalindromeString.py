def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome using two-pointer approach
    """
    if s is None or not s:
        return True

    i = 0
    j = len(s) - 1

    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


def palindrome(s: str) -> bool:
    """
    Check if string is palindrome using for-loop approach
    """
    if s is None or not s:
        return True

    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False

    return True


if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  # False (needs cleaning)
    print(is_palindrome("race a car"))  # False
    print(is_palindrome(None))  # True
    print(is_palindrome("abba"))  # True

    print(palindrome("A man a plan a canal Panama"))  # False
    print(palindrome("race a car"))  # False
    print(palindrome(None))  # True
    print(palindrome("abba"))  # True
