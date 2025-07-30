"""
     * <pre>
     * !Longest Substring Without Repeating Characters
     * Given a string s having lowercase characters, find the length of the longest substring without repeating characters.
     *
     * @param Examples:
     * Input: s = "geeksforgeeks"
     * Output: 7
     * Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.
     *
     * Input: s = "aaa"
     * Output: 1
     * Explanation: The longest substring without repeating characters is "a"
     *
     * Input: s = "abcdefabcbb"
     * Output: 6
     * Explanation: The longest substring without repeating characters is "abcdef".
     *
     * !Approach1: Visited Array(Time complexity: O(26 * n), Space complexity: O(1))
     * !ApproachII: Sliding Window + Set<> (Time complexity: O(n), Space complexity: O(1))
     * </pre>

"""


def longest_unique_substring(s: str) -> int:
    n = len(s)
    result = 0

    for i in range(n):
        # Initialize all characters as not visited
        visited = [False] * 26
        for j in range(i, n):
            # If current character is visited break the loop
            if visited[ord(s[j]) - ord('a')]:
                break
            else:
                # Else update result if this window is larger
                result = max(result, j - i + 1)
                visited[ord(s[j]) - ord('a')] = True
    return result


def longest_unique_substring_ii(s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)

    result = 0
    visited = [False] * 26

    # Left and Right pointer of sliding window
    left = 0
    for right in range(len(s)):
        while visited[ord(s[right]) - ord('a')]:
            visited[ord(s[left]) - ord('a')] = False
            left += 1

        visited[ord(s[right]) - ord('a')] = True
        # Update result with current window size
        result = max(result, right - left + 1)

    return result


def longest_palindrome_subsequence_iii(s: str) -> int:
    n = len(s)
    if n == 0 or n == 1:
        return n

    char_set = set()
    max_length = 0
    left = 0

    for right in range(n):
        current_char = s[right]
        while current_char in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(current_char)
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print("Expected: 7 ==", longest_palindrome_subsequence_iii("geeksforgeeks"))
    print("Expected: 6 ==", longest_palindrome_subsequence_iii("abcdefabcbb"))
    print("Expected: 1 ==", longest_palindrome_subsequence_iii("aaa"))
