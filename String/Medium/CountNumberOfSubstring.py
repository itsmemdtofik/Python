"""
    /**
     * <pre>
     * !Count substrings with k distinct characters
     * Given a string s consisting of lowercase characters and an integer k,
     * the task is to count all possible substrings (not necessarily distinct) that have exactly k distinct characters.
     *
     * @param Examples:
     * Input: s = "abc", k = 2
     * Output: 2
     * Explanation: Possible substrings are ["ab", "bc"]
     *
     * Input: s = "aba", k = 2
     * Output: 3
     * Explanation: Possible substrings are ["ab", "ba", "aba"]
     *
     * Input: s = "aa", k = 1
     * Output: 3
     * Explanation: Possible substrings are ["a", "a", "aa"]
     *
     * !Approach1: Checking All Substring(Time complexity: O(n^2), Space complexity: O(1))
     * !Approach2: Sliding Window(Time complexity: O(n), Space complexity: O(1))
     *
     * Step1: Use a sliding window with an array of size 26 to track character frequencies.
     * Step2: Expand the window to the right, adding characters.
     * Step3: Shrink the window from the left when distinct characters exceed k.
     * Step4: Count all valid substrings within the window.
     * Step5: Subtract substrings with k-1 distinct characters from k distinct characters.
     *
     * @param Formula: countExactK = countAtMostK − countAtMostKMinus1
     * </pre>
"""


def countSubstring(s: str, K: int) -> int:
    n = len(s)
    count = 0

    for i in range(n):
        visited = [False] * 26
        distinct_count = 0

        for j in range(i, n):
            idx = ord(s[j]) - ord('a')
            if not visited[idx]:
                visited[idx] = True
                distinct_count += 1

            if distinct_count == K:
                count += 1

    return count


def main():
    print("Expected: 2 == ", countSubstring("abc", 2))
    print("Expected: 3 == ", countSubstring("aba", 2))
    print("Expected: 3 == ", countSubstring("aa", 1))


if __name__ == "__main__":
    main()
