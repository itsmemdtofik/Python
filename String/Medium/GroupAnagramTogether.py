"""
     * <pre>
     * !Group Anagram Together
     * Given an array of words arr[], the task is to groups strings that are anagrams.
     * An anagram is a word or phrase formed by rearranging the letters of another,
     * using all the original letters exactly once.
     *
     * @param Example:
     * Input: arr[] = ["act", "god", "cat", "dog", "tac"]
     * Output: [["act", "cat", "tac"], ["god", "dog"]]
     * Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
     *
     * Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
     * Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]
     * Explanation:
     * Group 1: "abc", "bac" and "cab" are anagrams.
     * Group 2: "listen", "silent" and "enlist" are anagrams.
     * Group 3: "rat", "tar" and "art" are anagrams.
     *
     * !Approach1: Sorting(Time complexity: O(n*k*log(k)), Space complexity: O(n * k))
     * </pre>

"""

from collections import defaultdict


def group_anagrams(arr: list[str]) -> list[list[str]]:
    """Group anagrams together from a list of strings.

    Args:
        arr: List of strings to group

    Returns:
        List of grouped anagrams
    """
    anagram_map = defaultdict(list)

    for word in arr:
        # Sort the characters to form the key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    arr1 = ["act", "god", "cat", "dog", "tac"]
    print("Anagram groups are:", group_anagrams(arr1))

    arr2 = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
    print("Anagram groups are:", group_anagrams(arr2))
