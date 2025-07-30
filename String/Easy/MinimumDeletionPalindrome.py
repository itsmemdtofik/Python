"""
     * <pre>
     * !Minimum Deletion to Make a String Palindrome
     * Given a String s of length n, the task it to remove or delete the minimum number of
     * characters from the string so that the resultant string is palindrome.
     * @param Notes: The order of characters should be maintained
     *
     * Input: String s = "aebcbda"
     * Output: 2
     * Explanation: Remove characters 'e' and 'd' and resultant string will be "abcba"
     * which is a palindrome string.
     *
     * @param Formula: Minimum Deletion needed = Length of string - Length of its LPS = 7(aebcbda) - 5(abcba) = 2
     * Where, LPS = Longest Palindromic Subsequence (LPS)
     *
     * Input: String s = "aba"
     * Output: 0
     * Explanation: We dont remove any character
     *
     * !Approach: Using Recursion, Time complexity O(2 power n), Space complexity: O(n)
     * Step1: Compare the corner (left, right) characters first.
     * Step2: If the starting index i and ending index j of substring match, then recur for i + 1, j - 1.
     * Step3: Otherwise, recur for (i + 1, j) and (i, j - 1) and return the minimum out of these two plus 1.
     *
     * !Problem: Exponential Time
     * The recursive solution recomputes the same subproblems repeatedly, making it inefficient for larger strings (e.g., n > 20).
     * </pre>
"""


def min_deletions_to_palindrome(i: int, j: int, s: str) -> int:
    if i >= j:
        return 0

    if s[i] == s[j]:
        return min_deletions_to_palindrome(i + 1, j - 1, s)

    return 1 + min(min_deletions_to_palindrome(i + 1, j, s),
                   min_deletions_to_palindrome(i, j - 1, s))


def calc_min_deletion(s: str) -> int:
    if not s:
        return 0
    return min_deletions_to_palindrome(0, len(s) - 1, s)


def main():
    print("Minimum Deletion to make a String Palindrome:", calc_min_deletion("aebcbda"))
    print("Minimum Deletion to make a String Palindrome:", calc_min_deletion("aba"))
    print("Expected: 0 ==", calc_min_deletion("aba"))
    print("Expected: 4 ==", calc_min_deletion("abcde"))
    print("Expected: 2 ==", calc_min_deletion("aebcbda"))
    print("Expected: 0 ==", calc_min_deletion("z"))
    print("Expected: 0 ==", calc_min_deletion(""))
    print("Expected: 0 ==", calc_min_deletion("aaaaa"))
    print("Expected: 1 ==", calc_min_deletion("abccbaa"))


if __name__ == "__main__":
    main()
