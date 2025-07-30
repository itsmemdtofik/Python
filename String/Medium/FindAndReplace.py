"""
     * <pre>
     * !Find And Replace all occurrences of substring
     * Given three strings s, s1, and s2 of lengths n, m, and k respectively,
     * the task is to modify the string s by replacing all the substrings s1 with the string s2 in the string s
     *
     * !Approach: Time complexity O(n)
     * @param Examples:
     * Input: s = "abababa", s1 = "aba", s2 = "a"
     * Output: aba
     * Explanation: Change the substrings s[0, 2] and s[4, 6] to the string s2 modifies the string s to "aba".
     *
     * Input: s = "geeksforgeeks", s1 = "eek", s2 = "ok"
     * Output: goksforgoks
     * Explanation: Change the substrings s[1, 3] and s[9, 11] to the string
     * </pre>
"""


def replace_substring(s: str, s1: str, s2: str) -> str:
    """Find and replace all occurrences of substring s1 with s2 in string s.

    Args:
        s: The original string
        s1: The substring to be replaced
        s2: The replacement string

    Returns:
        The modified string with all occurrences of s1 replaced by s2
    """
    result = []
    i = 0
    m = len(s)
    n = len(s1)

    while i <= m - n:
        if s[i:i + n] == s1:
            result.append(s2)
            i += n
        else:
            result.append(s[i])
            i += 1

    # Append remaining characters
    result.append(s[i:])

    return ''.join(result)


if __name__ == "__main__":
    print("Expected: aba == ", replace_substring("abababa", "aba", "a"))
    print("Expected: goksforgoks == ", replace_substring("geeksforgeeks", "eek", "ok"))