"""
     * <pre>
     * !Longest Substring Without Repeating Characters
     * Given a string s, find the length of the longest substring without duplicate characters.
     * Example 1:
     * Input: s = "abcabcbb"
     * Output: 3
     * Explanation: The answer is "abc", with the length of 3.
     *
     * Example 2:
     * Input: s = "bbbbb"
     * Output: 1
     * Explanation: The answer is "b", with the length of 1.
     * </pre>

"""


# Using Set and Sliding Window
def slidingWindowUsingSet(s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)

    char_set = set()
    max_len = 0
    left = 0
    right = 0

    while right < len(s):
        current_char = s[right]
        while current_char in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(current_char)
        max_len = max(max_len, right - left + 1)
        right += 1

    return max_len


# Using HashMap and Sliding Window
def slidingWindowUsingHashMap(s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)

    char_map = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        current_char = s[right]

        # If character exists in current window, move left pointer
        if current_char in char_map:
            left = max(left, char_map[current_char] + 1)

        # Update the last index of current character
        char_map[current_char] = right

        # Calculate current window length
        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    test_cases = [
        "abcabcbb",  # Expected: 3
        "bbbbb",  # Expected: 1
        "   "  # Expected: 1 (spaces are duplicates)
    ]

    for i, s in enumerate(test_cases, 1):
        print(f"Test case {i}: \"{s}\"")
        print("Using Set + Sliding Window:", slidingWindowUsingSet(s))
        print("Using HashMap + Sliding Window:", slidingWindowUsingHashMap(s))
        print("-" * 40)


if __name__ == "__main__":
    main()
