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


def find_longest_word(s: str, dictionary: list[str]) -> str:
    longest_word = ""
    for word in dictionary:
        if is_subsequence(word, s):
            if (len(word) > len(longest_word) or
                    (len(word) == len(longest_word) and word < longest_word)):
                longest_word = word
    return longest_word


def is_subsequence(word: str, s: str) -> bool:
    i = j = 0
    while i < len(word) and j < len(s):
        if word[i] == s[j]:
            i += 1
        j += 1
    return i == len(word)


if __name__ == "__main__":
    print("Expected apple ==", find_longest_word("abpcplea",
                                                 ["ale", "apple", "monkey", "plea"]))

    print("Expected geeksgeeks ==", find_longest_word("geeksforgeeks",
                                                      ["pintu", "geeksfor", "geeksgeeks", "forgeek"]))
