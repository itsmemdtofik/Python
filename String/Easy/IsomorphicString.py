"""
     * <pre>
     * !Isomorphic:
     * Two String s1 and String s2 are called isomorphic if there is one to one mapping possible
     * For every character of String s1 to every character of String s2.
     * And all occurences of every character in s1 map to the same character in s2.
     *
     * !Example:
     * Input: String s1 = "aab", String s2 = "xxy"
     * Output: True
     * Explanation: 'a' is mapped to 'x' and 'b' is mapped to 'y'
     *
     * Input: String s1 = "aab", String s2 = "xyz"
     * Output: False
     * Explanation: One occurance of 'a' in String s1 has 'x' in
     * String s2 and other occurance of 'a' has 'y'.
     *
     * !Approach: Time complexity O(n), Space complexity O(n)
     * Step1: We mainly use two maps map1 and map2 to store characters as keys and their first indexes as values.
     * Step2: String must be in same length, Otherwise return false.
     * Step3: Iterate over the String s1 and String s2
     *        If the character is seen first time in s1, then store its index in map1.
     *        If the character is seen first time in s2, then store its index in map2.
     *        If Indexes in map for both the characters do not match, return false.
     * Step4: Return True
     *
     * </pre>
"""


def is_isomorphic(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    map1 = {}
    map2 = {}

    for i in range(len(s1)):
        if s1[i] not in map1:
            map1[s1[i]] = i
        if s2[i] not in map2:
            map2[s2[i]] = i

        if map1[s1[i]] != map2[s2[i]]:
            return False

    return True


print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("foo", "bar"))  # False
print(is_isomorphic("paper", "title"))  # True
print(is_isomorphic("ab", "aa"))  # False
