"""
     * <pre>
     * !Longest Substring with At Most K Distinct Characters
     * Given a string, find the length of the longest substring T that contains at most k distinct characters.
     * Example 1:
     * Input: s = "eceba", k = 2
     * Output: 3
     * Explanation: T is "ece" which its length is 3.
     *
     * Example 2:
     * Input: s = "aa", k = 1
     * Output: 2
     * Explanation: T is "aa" which its length is 2.
     * </pre>
"""


# This is not a proper sliding window solution caz O(n^2)
# This is not a proper sliding window solution caz O(n^2)
def longestKSubstring(s: str, K: int) -> int:
    result = -1
    seen = set()

    for i in range(len(s)):

        seen.clear()  # reset the set for new starting index - 'i'

        # Expand the window of substring from index i to j
        for j in range(i, len(s)):

            seen.add(s[j])
            if len(seen) == K:
                result = max(result, (j - i + 1))

            if len(seen) > K:
                break

    return result


# Lets solve it using the fully sliding window technique with O(n)
def slidingWindow(s: str, K: int) -> int:
    if not s or K <= 0:
        return -1

    freqMap = {}
    left = 0
    max_len = -1

    for right in range(len(s)):
        currentChar = s[right]
        freqMap[currentChar] = freqMap.get(currentChar, 0) + 1

        # Shrink the window if the number of unique characters exceeds K
        while len(freqMap) > K:
            left_char = s[left]
            freqMap[left_char] -= 1
            if freqMap[left_char] == 0:
                del freqMap[left_char]
            left += 1

        # Update the max_len if the current window has exactly K unique characters
        if len(freqMap) == K:
            max_len = max(max_len, right - left + 1)

    return max_len


def main():
    s1 = "aabacbebebe"
    k1 = 3
    print(longestKSubstring(s1, k1))  # Output: 7 ("cbebebe")

    s2 = "aaaa"
    k2 = 2
    print(longestKSubstring(s2, k2))  # Output: -1

    s3 = "aabaaab"
    k3 = 2
    print(longestKSubstring(s3, k3))  # Output: 7 ("aabaaab")

    print("Using Sliding Window:")
    s4 = "aabacbebebe"
    k4 = 3
    print(slidingWindow(s4, k4))  # Output: 7 ("cbebebe")

    s5 = "aaaa"
    k5 = 2
    print(slidingWindow(s5, k5))  # Output: -1

    s6 = "aabaaab"
    k6 = 2
    print(slidingWindow(s6, k6))  # Output: 7 ("aabaaab")

    print("Using Fixed Size Map:")
    print(slidingWindow(s1, k1))
    print(slidingWindow(s2, k2))
    print(slidingWindow(s3, k3))


if __name__ == "__main__":
    main()
