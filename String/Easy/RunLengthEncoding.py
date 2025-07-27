"""
     * <pre>
     * ! Solution Name : Run-Length Encoding (RLE) with Hexadecimal Count Representation
     * Run-Length Encoding (RLE): A basic compression technique where consecutive data elements are stored as a single value plus its count.
     * Example: "aaabbb" -> "a3b3"
     * ! Encrypt the String
     * ! Input: aaaaaaaaaaa, Output: ba
     *
     * !Approach:
     * Step1: Count consecutive character "aaaaaaaaaaa" -> "a11"
     * Step2: Convert frequency to hexadecimal "a11" -> "ab"
     * Step3: Reverse the string "ab" -> "ba"
     * </pre>
"""


class RunLengthEncoding:

    @staticmethod
    def rle(s: str) -> str:
        s = s.lower()
        if s is None or s == "":
            return ""

        sb = []
        i = 0

        while i < len(s):
            current_char = s[i]
            count = 1

            while i + 1 < len(s) and s[i + 1] == current_char:
                count += 1
                i += 1

            sb.append(current_char)
            if count <= 9:
                sb.append(str(count))
            else:
                sb.append(hex(count)[2:])  # Remove '0x' prefix

            i += 1

        return ''.join(sb)[::-1]  # Reverse the result string


# Test cases
if __name__ == '__main__':
    print("Expected ba == ", RunLengthEncoding.rle("aaaaaaaaaaa"))  # 11 a's → a + 'b' → reversed
    print("Expected 1c1b1a == ", RunLengthEncoding.rle("abc"))
    print("Expected 2f2e2d2c1b1a == ", RunLengthEncoding.rle("abccddeeffcc"))
    print("Expected null == ", RunLengthEncoding.rle(""))
    print("Expected 2a3b2a == ", RunLengthEncoding.rle("aabbbaa"))
    print("Expected 01a == ", RunLengthEncoding.rle("aaaaaaaaaaaaaaaa"))  # 16 a's → hex(16) = '10'
