"""
     * <pre>
     * !Check if Strings Are Rotations of Each Other
     * Given two string s1 and s2 of same length, the task is to check whether s2 is a rotation of s1.
     *
     * Input: s1 = "abcd", s2 = "cdab"
     * Output: true
     * Explanation: After 2 right rotations, s1 will become equal to s2.
     *
     * Input: s1 = "aab", s2 = "aba"
     * Output: true
     * Explanation: After 1 left rotation, s1 will become equal to s2.
     *
     * Input: s1 = "abcd", s2 = "acbd"
     * Output: false
     * Explanation: Strings are not rotations of each other.
     * </pre>
"""


def using_inbuilt_functionality(s1: str, s2: str) -> bool:
    """
    Check if s2 is a rotation of s1 by concatenating s1 with itself
    and checking if s2 is a substring.
    """
    if len(s1) != len(s2):
        return False
    doubled_s1 = s1 + s1
    print(doubled_s1)
    return s2 in doubled_s1


def generating_all_rotations(s1: str, s2: str) -> bool:
    """
    Check all possible rotations of s1 to see if any match s2.
    """
    if len(s1) != len(s2):
        return False

    n = len(s1)
    for i in range(n):
        if s1 == s2:
            return True

        # Right rotate s1
        last_char = s1[-1]
        s1 = last_char + s1[:-1]

    return False


if __name__ == "__main__":
    print(using_inbuilt_functionality("abcd", "cdab"))  # True
    print(generating_all_rotations("abcd", "cdab"))  # True
