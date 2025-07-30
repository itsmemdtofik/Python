"""
     * <pre>
     * !Count Distinct Subsequences
     * Given a String s, your task is to find the count distinct subsequences of it.
     *
     * Input: String s = "gfg"
     * Output: 7
     * Explanation: The seven distinct subsequences are: "", "g", "f", "gf", "fg", "gg" and "gfg"
     *
     * Input: String s = "ggg"
     * Output: 4
     * Explanation: The four distinct subsequences are: "", "g", "gg" and "ggg"
     *
     * !Approach: Time complexity O(n), Space complexity O(n)
     * Step1: Create an array of dp[] of size n + 1, and initialize dp[0] with 1.
     * Step2: Create an array last[] of size 26, to store the index of last occurence of each character.
     * Step3: Start iterating from index 1 to n, and for each index dp[i] = 2 * dp[i - 1] - dp[last(s.charAt[i - 1])].
     * Step4: Update last[s.charAt(i - 1)] to i - 1.
     * Step5: At last dp[n] stores the required result.
     * </pre>
"""


def count_distinct_sub_seq(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty subsequence

    last = [-1] * 26  # Track last occurrence of each character (a-z)

    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]

        char_index = ord(s[i - 1]) - ord('a')
        if last[char_index] != -1:
            dp[i] -= dp[last[char_index]]

        last[char_index] = i - 1

    return dp[n]


if __name__ == "__main__":
    print("Distinct SubSeq is:", count_distinct_sub_seq("gfg"))  # Output: 7
    print("Distinct SubSeq is:", count_distinct_sub_seq("ggg"))  # Output: 4
