"""
     * <pre>
     * !Longest Palindromic Subsequence(LPS)
     * Given a string s, find the length of the Longest Palindromic Subsequence in it.
     * &#64;param Note: The LPS is the maximum-length subsequence of a given string that is also a Palindrome.
     *
     * @param Example:
     *
     * String s = "BANANA"
     * size2: AA, NN
     * size3: ANA, NAN, AAA
     * size4: ANNA
     * size5: ANANA -> LPS
     *
     * Input: s = "bbabcbcab"
     * Output: 7
     * Explanation: Subsequence "babcbab" is the longest subsequence which is also a palindrome.
     *
     * Input: s = "abcd"
     * Output: 1
     * Explanation: "a", "b", "c" and "d" are palindromic and all have a length 1.
     *
     * !Approach1: Recursion(Time complexity : O(2^n), Space complexity: O(1))
     * !Approach2: Dynamic Programming(Tabulation: Time & Space = O(n^2))
     * </pre>

"""


def lps(s: str, low: int, high: int) -> int:
    """Recursive solution for longest palindromic subsequence"""
    # Base Case
    if low > high:
        return 0

    # If there is only one character
    if low == high:
        return 1

    # If first and last character match
    if s[low] == s[high]:
        return lps(s, low + 1, high - 1) + 2

    # If the first and last character do not match
    return max(lps(s, low, high - 1), lps(s, low + 1, high))


def longest_palindrome_subsequence(s: str) -> int:
    """Wrapper function for recursive solution"""
    return lps(s, 0, len(s) - 1)


def longest_palindrome_subsequence_ii(s: str) -> int:
    """Dynamic programming solution"""
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Build the DP table for all substrings
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # If there is only one character
            if i == j:
                dp[i][j] = 1
                continue

            # If characters at position i and j are the same
            if s[i] == s[j]:
                if i + 1 == j:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Otherwise, take the maximum length from either excluding i or j
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The final answer is stored in dp[0][n-1]
    return dp[0][n - 1]


if __name__ == "__main__":
    print("Expected: 7 ==", longest_palindrome_subsequence("bbabcbcab"))
    print("Expected: 1 ==", longest_palindrome_subsequence("abcd"))

    print("Expected: 7 ==", longest_palindrome_subsequence_ii("bbabcbcab"))
    print("Expected: 1 ==", longest_palindrome_subsequence_ii("abcd"))
