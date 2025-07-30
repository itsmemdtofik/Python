"""
     * <pre>
     * !Minimum Deletion to Make a String Palindrome
     * Given a String s of length n, the task it to remove or delete the minimum number of
     * characters from the string so that the resultant string is palindrome.
     * @param Notes: The order of characters should be maintained
     *
     * @param Optimization: Iterative OR Tabulation (Bottom-Up DP)
     * To avoid recomputation, cache results of subproblems using a memo table.
     *
     * !Time complexity O(n2), Space complexity: O(n2), OR O(n)
     * @param Formula: Minimum Deletion needed = Length of string - Length of its LPS = 7(aebcbda) - 5(abcba) = 2
     * Where, LPS = Longest Palindromic Subsequence (LPS)
     * </pre>
"""


def min_deletions_to_palindrome(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]  # Initialize DP table with zeros

    for i in range(n - 1, -1, -1):  # Start from end of string
        for j in range(i, n):  # End pointer moves forward
            if i == j:
                dp[i][j] = 0  # Single character is palindrome
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


if __name__ == "__main__":
    print("Minimum Deletion to make a String Palindrome:", min_deletions_to_palindrome("aebcbda"))
    print("Minimum Deletion to make a String Palindrome:", min_deletions_to_palindrome("aba"))
    # Additional test cases
    print("Expected: 0 ==", min_deletions_to_palindrome("racecar"))
    print("Expected: 2 ==", min_deletions_to_palindrome("aebcbda"))
    print("Expected: 3 ==", min_deletions_to_palindrome("abcd"))
