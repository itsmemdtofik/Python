"""
     * <pre>
     * !Check if a String is Interleaving of Other Two
     * Give three strings s1, s2 and s3, determine if s3 is formed by interleaving s1 and s2.
     * A string s3 is an interleaving of s1 and s2 if:
     *        1. It contains all characters of s1 and s2 while preserving their relative order.
     *        2. Characters from s1 and s2 appear in s3 in the same order as in their original strings.
     *        3. The length of s3 equals the combined length of s1 and s2.
     *
     * @param Examples:
     *
     * Input: String s1 = "AAB",  s2 = "AAC",  s3 =  "AAAABC"
     * Output: true
     * Explanation: The string "AAAABC" has all characters of the other two strings and in the same order.
     *
     * Input: String s1 = "AB",  s2 = "C",  s3 =  "ACB"
     * Output: true
     * Explanation: s3 has all characters of s1 and s2 and retains order of characters of s1.
     *
     * Input: String s1 = "YX",  s2 = "X", s3 = "XXY"
     * Output:  false
     * Explanation: "XXY " is not interleaved of "YX" and "X".  The strings that can be formed are YXX and XYX
     *
     * !Approach1: Recursion(Time complexity: O(2^(m+n)), Space complexity: O(m+n))
     * !Approach2: Memoization or DP(Time complexity(O(m*n), Space complexity: O)
     *
     * </pre>
"""


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    """Check if s3 is formed by interleaving s1 and s2.

    Args:
        s1: First input string
        s2: Second input string
        s3: String to check for interleaving

    Returns:
        True if s3 is interleaving of s1 and s2, False otherwise
    """
    if len(s1) + len(s2) != len(s3):
        return False

    return is_interleave_recursive(s1, s2, s3, 0, 0, 0)


def is_interleave_recursive(s1: str, s2: str, s3: str, i: int, j: int, k: int) -> bool:
    """Recursive helper function for is_interleave."""
    # Base case: all strings fully traversed
    if i == len(s1) and j == len(s2) and k == len(s3):
        return True

    # If we've reached the end of s3 but not s1 and s2
    if k == len(s3):
        return False

    result = False

    # Try taking current character from s1 if it matches s3
    if i < len(s1) and s1[i] == s3[k]:
        result = is_interleave_recursive(s1, s2, s3, i + 1, j, k + 1)

    # Try taking current character from s2 if it matches s3 and s1 didn't match
    if not result and j < len(s2) and s2[j] == s3[k]:
        result = is_interleave_recursive(s1, s2, s3, i, j + 1, k + 1)

    return result


if __name__ == "__main__":
    print("Expected: True ==", is_interleave("AAB", "AAC", "AAAABC"))
    print("Expected: True ==", is_interleave("AB", "C", "ACB"))
    print("Expected: False ==", is_interleave("YX", "X", "XXY"))
    print("Expected: True ==", is_interleave("aaa", "aaa", "aaaaaa"))
