"""
 * <pre>
 * !ATOI: String To Integer
 * Convert a string to an integer. Handles leading/trailing spaces, signs, and valid numeric characters.
 *
 * @param Examples:
 * Input: s = "   -"
 * Output: 0
 * Explanation: No digits are present, therefore 0.
 *
 * Input: s = "  1231231231311133"
 * Output: 2147483647
 * Explanation: The converted number is greater than 231 - 1, therefore print 231 - 1 = 2147483647.
 *
 * Input: s = "-999999999999"
 * Output: -2147483648
 * Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.
 *
 * Input: s = "  -0012gfg4"
 * Output: -12
 * Explanation: Nothing is read after -12 as a non-digit character 'g' was encountered.
 *
 * !Approach:  Time complexity O(n), Space complexity O(1)
 * Step1: Skip the leading whitespaces by iterating from the first character.
 * Step2: Now, check for at most one sign character ('+' or '-') and maintain a sign variable to keep track of the sign of the number.
 * Step3: Finally read all the digits and construct the number until the first non-digit character is encountered or end of the number.
 * Step4: While constructing the number, check if the number becomes greater than 2^31 -1, print 2^31 -1, similarly if the number becomes less than -2^31, print -2^31
 * </pre>
"""


def atoi(s: str) -> int:
    sign = 1
    res = 0
    idx = 0
    n = len(s)

    # Skip leading whitespace
    while idx < n and s[idx] == ' ':
        idx += 1

    # Handle optional sign
    if idx < n and (s[idx] == '-' or s[idx] == '+'):
        sign = -1 if s[idx] == '-' else 1
        idx += 1

    # Process digits
    while idx < n and s[idx].isdigit():
        digit = int(s[idx])

        # Check for integer overflow
        if res > (2 ** 31 - 1) // 10 or (res == (2 ** 31 - 1) // 10 and digit > 7):
            return (2 ** 31 - 1) if sign == 1 else -2 ** 31

        res = 10 * res + digit
        idx += 1

    return res * sign


if __name__ == "__main__":
    print("Expected -123 ==", atoi("-123"))
    print("Expected 0 ==", atoi(" -"))
    print("Expected 2147483647 ==", atoi("1231231231311133"))
    print("Expected -2147483648 ==", atoi("-999999999999"))
    print("Expected -12 ==", atoi("-0012gfg4"))
