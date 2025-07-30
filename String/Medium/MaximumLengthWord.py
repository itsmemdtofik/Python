"""
     * <pre>
     * !Maximum Length Word in Dictionary
     * Giving a dictionary and a String s, find the maximum length string in dictionary
     * which can be formed by deleting some characters of the given String s.
     *
     * &#64;param Examples:
     * Input: dict = [ "ale", "apple", "monkey", "plea" ],  str ="abpcplea"
     * Output: 5(apple), character is 5
     * Explanation: On removing characters at indexes 1,3,7 we can form string "apple" ,
     * similarly we can form strings "ale" and "plea" also, but "apple" is the longest string so we return "apple".
     *
     * Input: dict = [ "pintu", "geeksfor", "geeksgeeks", " forgeek" ],  str ="geeksforgeeks"
     * Output: 10(geeksgeeks)
     * Explanation: On removing characters at indexes 5,6,7 we can form string "geeksgeeks" ,
     * similarly we can form strings "geeksfor" and "forgeeks" also, but "geeksgeeks" is the longest string so we return "geeksgeeks" .
     *
     * !Approach: Time complexity O(D * ( L + N)), Space complexity: O(1)
     * @param where D = Dictionary, L = length of the current word, N = length of the String s
     *
     * Step1: Iterate over each word in DICTIONARY and store the longestWord
     * Step2: Check if word is a Subsequence of String s, use two pointer to verify it.
     * Step3: Update the longestWord, if word is a valid subsequence.
     * Step4: Return the result
     *
     * </pre>
"""


def find_longest_word(d: list[str], s: str) -> int:
    longest_word_length = 0
    d.sort()  # Sort the dictionary lexicographically

    for word in d:
        if is_subsequence(word, s) and len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length


def is_subsequence(d_word: str, s_word: str) -> bool:
    i = j = 0
    while i < len(d_word) and j < len(s_word):
        if d_word[i] == s_word[j]:
            i += 1
        j += 1
    return i == len(d_word)


if __name__ == "__main__":
    print("Expected 5 ==", find_longest_word(["ale", "apple", "monkey", "plea"], "abpcplea"))
    print("Expected 10 ==", find_longest_word(["pintu", "geeksfor", "geeksgeeks", "forgeek"], "geeksforgeeks"))
