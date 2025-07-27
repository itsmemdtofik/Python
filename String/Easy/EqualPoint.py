"""
     * <pre>
     * ! Find an equal point in a string of brackets
     * ! Time Complexity: O(n), Space complexity O(1)
     * Input: "(())))("
     * Output: 4
     * Explanation: After index 4, string splits into (()) and ))(.
     * The number of opening brackets in the first part is equal to the number of closing brackets in the second part.
     *
     * Input: str = "))"
     * Output: -1 (No such index exists)
     *
     * !Solution:
     * Step1 : Pre calculate the number of closing brackets.
     * Step2: We update the counts of opening and closing brackets at every index as we traverse the string, and when they are equal, we return the index .
     * Step3: if no such index exists we return -1.
     * </pre>
"""


class BalancePoint:

    @staticmethod
    def equal_point(s: str) -> int:
        if s is None or s == "":
            return -1

        open_count = 0
        close_count = 0

        # Count total closing brackets
        for char in s:
            if char == ')':
                close_count += 1

        # Traverse to find the balance point
        for i in range(len(s)):
            if open_count == close_count:
                return i
            elif s[i] == '(':
                open_count += 1
            elif s[i] == ')':
                close_count -= 1

        return -1


# Test cases
if __name__ == '__main__':
    s = "(())))("
    print("Expected 4 :", BalancePoint.equal_point(s))

    s1 = "))"
    print("Expected -1 :", BalancePoint.equal_point(s1))
