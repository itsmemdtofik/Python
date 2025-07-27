"""
     * <pre>
     * !First non-repeating character of given string
     * Given a string s of lowercase English letters, the task is to find the first non-repeating character.
     * If there is no such character, return '$'.
     *
     * Input: s = "geeksforgeeks"
     * Output: 'f'
     * Explanation: 'f' is the first character in the string which does not repeat.
     *
     * Input: s = "racecar"
     * Output: 'e'
     * Explanation: 'e' is the only character in the string which does not repeat.
     *
     * Input: "aabbccc"
     * Output: '$'
     * Explanation: All the characters in the given string are repeating.
     *
     * Step 1: Count the frequency of each character
     * Step 2: Find the first non-repeating character
     * Step 3: If no non-repeating character exists, return -1
     * </pre>
"""


class FirstNonRepeating:

    @staticmethod
    def first_unique_char(s: str) -> int:
        char_count = {}

        # Count frequency of each character
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        # Find first non-repeating character's index
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i

        return -1

    @staticmethod
    def using_nested_loop(s: str) -> str:
        n = len(s)

        for i in range(n):
            found = False
            for j in range(n):
                if i != j and s[i] == s[j]:
                    found = True
                    break
            if not found:
                return s[i]

        return '$'


if __name__ == '__main__':
    print("First Non-Repeating or Unique character \"leetcode\" is :", FirstNonRepeating.first_unique_char("leetcode"))
    print("First Non-Repeating or Unique character \"loveleetcode\" is :",
          FirstNonRepeating.first_unique_char("loveleetcode"))
    print("First Non-Repeating or Unique character \"aabb\" is :", FirstNonRepeating.first_unique_char("aabb"))

    print("First non-repeating character is:", FirstNonRepeating.using_nested_loop("geeksforgeeks"))
