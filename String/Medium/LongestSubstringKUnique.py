"""
     * <pre>
     * !Longest substring with k unique characters
     * Given a string you need to print longest possible substring that has exactly k unique characters.
     * If there is more than one substring of longest possible length, then print any one of them.
     *
     * @param Note: Source(Google Interview Question).
     *
     * @param Examples:
     * Input: Str = "aabbcc", k = 1
     * Output: 2
     * Explanation: Max substring can be any one from ["aa" , "bb" , "cc"].
     *
     * Input: Str = "aabbcc", k = 2
     * Output: 4
     * Explanation: Max substring can be any one from ["aabb" , "bbcc"].
     *
     * !Approach: Sliding Window Technique: O(n) Time and O(1) Space
     * We maintain a window that can expand and shrink based on the number of unique characters within it.
     * </pre>
"""
from collections import defaultdict


def longest_substring_with_k_unique(s: str, k: int) -> str:
    if not s or k <= 0:
        return "-1"

    char_count = defaultdict(int)
    left = 0  # Left pointer of the sliding window
    max_length = 0  # Length of the longest valid substring found
    start = 0  # Starting index of the longest valid substring

    for right in range(len(s)):
        current_char = s[right]
        char_count[current_char] += 1

        # If the number of unique characters exceeds k, move the left pointer
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        # If current window has exactly k unique characters and is the longest so far
        if len(char_count) == k and (right - left + 1) > max_length:
            max_length = right - left + 1
            start = left

    # Return the result
    return s[start:start + max_length] if max_length != 0 else "-1"


if __name__ == "__main__":
    print(longest_substring_with_k_unique("aabbcc", 1))  # Output: "aa" or "bb" or "cc"
    print(longest_substring_with_k_unique("aabbcc", 2))  # Output: "aabb" or "bbcc"
    print(longest_substring_with_k_unique("aabbcc", 3))  # Output: "aabbcc"
    print(longest_substring_with_k_unique("aaabbb", 3))  # Output: "-1"
