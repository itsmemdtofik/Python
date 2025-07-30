"""
     * <pre>
     * !Longest prefix which is also suffix
     * Given a string s, the task is to find the length of the longest proper prefix which is also a suffix.
     * A proper prefix is a prefix that doesn’t include whole string.
     * For example, prefixes of "abc" are "", "a", "ab" and "abc" but proper prefixes are "", "a" and "ab" only.
     *
     * @param Examples:
     * Input: s = "aabcdaabc"
     * Output: 4
     * Explanation: The string "aabc" is the longest proper prefix which is also the suffix.
     *
     * Input: s= "ababab"
     * Output: 4
     * Explanation: The string "abab" is the longest proper prefix which is also the suffix.
     *
     * Input: s = "aaaa"
     * Output: 3
     * Explanation: The string "aaa" is the longest proper prefix which is also the suffix.
     *
     * !Approach: Comparing each Proper Prefix with Suffix - O(n^2) Time and O(1) Space
     * </pre>
"""


def longest_prefix_suffix(s: str) -> int:
    """KMP algorithm approach (O(n) time)"""
    n = len(s)
    lps = [0] * n
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps[n - 1]


def longest_prefix_suffix_ii(s: str) -> int:
    """Naive approach (O(n²) time)"""
    res = 0
    n = len(s)

    # Iterating over all possible lengths
    for length in range(1, n):
        # Starting index of suffix
        j = len(s) - length

        flag = True

        # Comparing proper prefix with suffix of length 'length'
        for k in range(length):
            if s[k] != s[j + k]:
                flag = False
                break

        # If they match, update the result
        if flag:
            res = length

    return res


if __name__ == "__main__":
    print("Expected: 4 ==", longest_prefix_suffix("aabcdaabc"))
    print("Expected: 4 ==", longest_prefix_suffix("ababab"))
    print("Expected: 3 ==", longest_prefix_suffix("aaaa"))

    print("Expected: 4 ==", longest_prefix_suffix_ii("aabcdaabc"))
    print("Expected: 4 ==", longest_prefix_suffix_ii("ababab"))
    print("Expected: 3 ==", longest_prefix_suffix_ii("aaaa"))
