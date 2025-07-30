"""
     * <pre>
     * !Minimum Deletion to Make a String Palindrome
     * Given a String s of length n, the task it to remove or delete the minimum number of
     * characters from the string so that the resultant string is palindrome.
     * @param Notes: The order of characters should be maintained
     *
     * @param Optimization: Memoization (Top-Down DP)
     * To avoid recomputation, cache results of subproblems using a memo table.
     *
     * !Time complexity O(n2), Space complexity: O(n2)
     *
     * @param Formula: Minimum Deletion needed = Length of string - Length of its LPS = 7(aebcbda) - 5(abcba) = 2
     * Where, LPS = Longest Palindromic Subsequence (LPS)
     * </pre>
"""


def min_deletions_palindrome(i: int, j: int, s: str, memo: list) -> int:
    if i >= j:
        return 0

    if memo[i][j] is not None:
        return memo[i][j]  # Return cached result

    if s[i] == s[j]:
        memo[i][j] = min_deletions_palindrome(i + 1, j - 1, s, memo)
    else:
        memo[i][j] = 1 + min(
            min_deletions_palindrome(i + 1, j, s, memo),
            min_deletions_palindrome(i, j - 1, s, memo)
        )
    return memo[i][j]


def calc_min_deletion(s: str) -> int:
    if not s:
        return 0
    n = len(s)
    # Initialize memoization table with None
    memo = [[None for _ in range(n)] for _ in range(n)]
    return min_deletions_palindrome(0, n - 1, s, memo)


if __name__ == "__main__":
    print("Minimum Deletion to make a String Palindrome:", calc_min_deletion("aebcbda"))
    print("Minimum Deletion to make a String Palindrome:", calc_min_deletion("aba"))
    print("Expected: 0 ==", calc_min_deletion("aba"))
    print("Expected: 4 ==", calc_min_deletion("abcde"))
    print("Expected: 2 ==", calc_min_deletion("aebcbda"))
    print("Expected: 0 ==", calc_min_deletion("z"))
    print("Expected: 0 ==", calc_min_deletion(""))
    print("Expected: 0 ==", calc_min_deletion("aaaaa"))
    print("Expected: 1 ==", calc_min_deletion("abccbaa"))
