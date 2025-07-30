"""
     * <pre>
     * !Valid Palindrome String : Two Pointer Approach
     *
     * Input: A man, a plan, a canal: Panama
     * Output: True
     * Explanation: If we reverse the string we get the same string.
     * </pre>
"""

import re


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a valid palindrome using two-pointer approach.
    Ignore non-alphanumeric characters and case differences.
    """
    if s is None or not s:
        return True

    i = 0
    j = len(s) - 1

    while i <= j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

    return True


def is_palindrome_regex(s: str) -> bool:
    """
    Alternative version using regex for cleaning the string first
    """
    if s is None:
        return True

    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))  # False
    print(is_palindrome(None))  # True
    print(is_palindrome("s"))  # True

    # Test regex version
    print(is_palindrome_regex("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome_regex("race a car"))  # False
