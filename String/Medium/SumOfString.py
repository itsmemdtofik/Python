"""
     * <pre>
     * !Sum Of Two Large Numbers as String
     * Given two numbers as strings.
     * The numbers may be very large (may not fit in long long int),
     * the task is to find sum of these two numbers.
     *
     * @param Examples:
     * Input: s1 = "23", s2 = "25"
     * Output: "48"
     *
     * Input: s1 = "00", s2 = "000"
     * Output: "0"
     *
     * Input: s1 = "10000000", s2 = "89990000"
     * Output: 99990000
     *
     * !Approach: Time complexity O(n + m), Space complexity O(max(n, m))
     * Step1: Start from the end of both strings and process each digit.
     * Step2: Add corresponding digits from both strings along with any carry from the previous addition.
     * Step3: Store the result digit and update the carry for the next iteration.
     * Step4: After processing all digits, if there's any remaining carry, add it to the result.
     * Step5: Reverse the result string since we processed digits from least significant to most significant.
     * </pre>
"""


def sum_of_string_as_string(num1: str, num2: str) -> str:
    if not num1:
        return num2
    if not num2:
        return num1

    result = []
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry > 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))

        i -= 1
        j -= 1

    # Remove leading zeros (except for single "0")
    while len(result) > 1 and result[-1] == '0':
        result.pop()

    return ''.join(reversed(result))


if __name__ == "__main__":
    print("Expected: 48 ==", sum_of_string_as_string("23", "25"))
    print("Expected: 0 ==", sum_of_string_as_string("00", "000"))
    print("Expected: 99990000 ==", sum_of_string_as_string("10000000", "89990000"))
