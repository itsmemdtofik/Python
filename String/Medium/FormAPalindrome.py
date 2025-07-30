"""
     * <pre>
     * !Minimum insertions to form a palindrome
     * Given a string s, the task is to find the minimum number of characters to be inserted to convert it to a palindrome.
     *
     * @param Examples:
     *
     * Input: s = "geeks"
     * Output: 3
     * Explanation: "skgeegks" is a palindromic string, which requires 3 insertions.
     * Let's take s = "geeks":
     * All possible palindromic subsequences:
     * Length 1: g, e, k, s
     * Length 2: ee
     * The Longest Palindromic Subsequence is "ee" → length = 2
     * Minimum Insertions = 5 − 2 = 3
     *
     * !Approach: Time complexity O(n2), Space complexity O(n2)
     * Step1: Let n be the length of string
     * Step2: Let LPS be the length of the longest palindromic subsequence.
     * Step3: Minimum insertions needed = n - LPS.
     *
     * @param Notes: Minimum Insertions = Length of String − Length of LPS
     * </pre>
"""


def min_insertions(s: str) -> int:
    """Calculate minimum insertions needed to form a palindrome.

    Args:
        s: Input string

    Returns:
        Minimum number of insertions required to make the string a palindrome
    """
    n = len(s)
    lps = longest_palindromic_subseq(s)
    return n - lps


def longest_palindromic_subseq(s: str) -> int:
    """Find the length of the longest palindromic subsequence.

    Args:
        s: Input string

    Returns:
        Length of the longest palindromic subsequence
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


if __name__ == "__main__":
    print("Expected: 3 ==", min_insertions("geeks"))
    print("Expected: 3 ==", min_insertions("abcd"))
    print("Expected: 0 ==", min_insertions("aba"))
