"""
     * <pre>
     * !Check If Two Strings are K-Anagram or not
     * Two Strings are called k-anagrams if the following conditions are true:
     *      1. Both have same number of character
     *      2. Two strings can become anagram by changing at most K-character in a string
     *
     * Example:
     * Input: String s1 = "anagram" , String s2 = "grammar" , K = 3
     * Output: True
     * Explanation: We can update maximum 3 values and it can be done in changing only 'r' to 'n'.
     *
     * !Approach: HashMap, Time complexity O(n), Space complexity: O(1)
     * Step1: Create a frequency map for the String s1 by storing character counts.
     * Step2: Iterate through the String s2, reducing the count of matching characters in the map (to find difference).
     * Step3: Finally, sum the remaining frequencies in the map,
     * And if the difference exceeds K (difference <= K), return false; otherwise, return true.
     * </pre>

"""

from collections import defaultdict


def kth_anagram(s1: str, s2: str, K: int) -> bool:
    if s1 is None or s2 is None:
        return False

    if len(s1) != len(s2):
        return False

    if K < 0:
        return False

    if K >= len(s1):
        return True

    freq_map = defaultdict(int)
    for ch in s1:
        freq_map[ch] += 1

    for ch in s2:
        freq_map[ch] -= 1

    difference = 0
    for count in freq_map.values():
        if count > 0:
            difference += count

    return difference <= K


if __name__ == "__main__":
    print("Expected True:", kth_anagram("anagram", "grammar", 3))  # True
    print("Expected False:", kth_anagram("geeks", "eggkf", 1))  # False
    print("Expected True:", kth_anagram("abc", "def", 3))  # True
    print("Expected False:", kth_anagram(None, "test", 1))  # False
