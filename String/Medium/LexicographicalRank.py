"""
     * <pre>
     * !Lexicographic rank of a String
     * Given a string str, find its rank among all its permutations when sorted lexicographically.
     * @param Note: The characters in string are all unique.
     *
     * Examples:
     * Input: str = "acb"
     * Output: 2
     * Explanation: If all the permutations of the string are arranged lexicographically
     * they will be "abc", "acb", "bac", "bca", "cab", "cba". From here it can be clearly that the rank of str is 2.
     *
     * Input: str = "string"
     * Output: 598
     *
     * Input: str[] = "cba"
     * Output: Rank = 6
     * !Approach:
     * </pre>
"""


def find_rank(s: str) -> int:
    rank = 1
    n = len(s)

    # Precompute factorial values
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if s[j] < s[i]:
                count += 1
        rank += count * fact[n - i - 1]

    return rank


if __name__ == "__main__":
    str1 = "acb"
    print(f"Expected: 2 == {find_rank(str1)}")

    str2 = "string"
    print(f"Expected: 598 == {find_rank(str2)}")

    str3 = "cba"
    print(f"Expected: 6 == {find_rank(str3)}")
