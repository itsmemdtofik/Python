"""
     * <pre>
     * !Minimum Repetitions of s1 such that s2 is a substring of it.
     * Given two strings s1 and s2, the task is to find the minimum number of times
     * s1 has to be repeated such that s2 is a substring of it. If no such solution exists, print -1.
     *
     * @param Examples:
     *
     * Input: s1 = "abcd", s2 = "cdabcdab"
     * Output: 3
     * Explanation: After repeating s1 three times, s1 will become “abcdabcdabcd”.
     * Now, s2 is now a substring of s1 = "abcdabcdabcd".
     * Also s2 is not a substring of s1 when it is repeated less than 3 times.
     *
     * Input: s1 = "ab", s2 = "cab"
     * Output : -1
     * Explanation: s2 can not become a substring of s1 after any repetition of s1.
     * </pre>

"""


def repeated_string_match(s1: str, s2: str) -> int:
    if s1 is None or s2 is None:
        return -1
    if not s2:
        return 1
    if not s1:
        return -1

    count = 0
    sb = []
    max_repetitions = (len(s2) // len(s1)) + 2

    while count <= max_repetitions:
        sb.append(s1)
        count += 1
        current_str = ''.join(sb)
        if s2 in current_str:
            return count

    return -1


if __name__ == "__main__":
    print("Expected: 3 ==", repeated_string_match("abcd", "cdabcdab"))
    print("Expected: -1 ==", repeated_string_match("ab", "cab"))
    print("Expected: 2 ==", repeated_string_match("a", "aa"))
    print("Expected: 4 ==", repeated_string_match("abc", "cabcabca"))
    print("Expected: -1 ==", repeated_string_match("", "a"))
    print("Expected: 1 ==", repeated_string_match("a", ""))
