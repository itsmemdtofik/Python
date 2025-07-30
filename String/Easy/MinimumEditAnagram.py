from collections import defaultdict


def min_edit_anagram(str1: str, str2: str) -> int:
    """
    Calculate minimum edits to make two strings anagrams of each other.
    Time complexity: O(n), Space complexity: O(n)
    """
    str1 = str1.lower()
    str2 = str2.lower()

    freq_map = defaultdict(int)

    # Count characters in str1
    for ch in str1:
        freq_map[ch] += 1

    # Subtract characters in str2
    for ch in str2:
        freq_map[ch] -= 1

    # Sum absolute differences
    count = 0
    for val in freq_map.values():
        count += abs(val)

    return count


if __name__ == "__main__":
    s1 = "abc"
    s2 = "cde"
    print("Minimum edits:", min_edit_anagram(s1, s2))  # Output: 4

    s1 = "hello"
    s2 = "billion"
    print("Minimum edits:", min_edit_anagram(s1, s2))  # Output: 6
