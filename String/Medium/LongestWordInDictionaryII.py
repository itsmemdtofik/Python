"""
     * <pre>
     * !Largest Word in Dictionary
     * Giving a dictionary and a String s, find the longest string in dictionary
     * which can be formed by deleting some characters of the given String s.
     *
     * @param Examples:
     * Input: dict = [ "ale", "apple", "monkey", "plea" ],  str ="abpcplea"
     * Output: apple
     * Explanation: On removing characters at indexes 1,3,7 we can form string "apple" ,
     * similarly we can form strings "ale" and "plea" also, but "apple" is the longest string so we return "apple".
     *
     * Input: dict = [ "pintu", "geeksfor", "geeksgeeks", " forgeek" ],  str ="geeksforgeeks"
     * Output: geeksgeeks
     * Explanation: On removing characters at indexes 5,6,7 we can form string "geeksgeeks" ,
     * similarly we can form strings "geeksfor" and "forgeeks" also, but "geeksgeeks" is the longest string so we return "geeksgeeks" .
     *
     * !Approach: Using Sorting Time complexity O(n^2 Log (n)), Space complexity: O(1)
     *
     * Step1: Sort the dictionary word and traverse all dictionary words and for every word.
     * Step2: Check if word is a Subsequence of String s, use two pointer to verify it.
     * Step3: Update the longestWord, if word is a valid subsequence.
     * Step4: Return the longestWord
     *
     * </pre>
"""


def find_longest_word(d: list[str], s: str) -> str:
    longest_word = ""
    d.sort()  # Sort the dictionary lexicographically

    for word in d:
        if is_subsequence(word, s) and len(word) > len(longest_word):
            longest_word = word
    return longest_word


def is_subsequence(d_word: str, s_word: str) -> bool:
    i = j = 0
    while i < len(d_word) and j < len(s_word):
        if d_word[i] == s_word[j]:
            i += 1
        j += 1
    return i == len(d_word)


if __name__ == "__main__":
    print("Expected apple ==", find_longest_word(["ale", "apple", "monkey", "plea"], "abpcplea"))
    print("Expected geeksgeeks ==", find_longest_word(["pintu", "geeksfor", "geeksgeeks", "forgeek"], "geeksforgeeks"))
