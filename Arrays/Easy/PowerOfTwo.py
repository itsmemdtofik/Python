"""
     * ! Is Power Of Two : Time complexity O(1) Space complexity: O(1)
     * ! Approach: Bitwise Operation
     * * A number is a power of two if it has exactly 1 in its binary representation.
     * * Example 1:
     * 2 -> 10 (Binary)
     * 4 -> 100 (Binary)
     * 8 -> 1000 (Binary)
     *
     * * Example Walkthrough
     * Power of Two (8):
     * Binary: 8 = 1000
     * 8-1 = 7 = 0111
     * 1000 & 0111 = 0000 → Returns true
"""


def isPowerOfTwo(number):
    if number is None:
        return None
    if number <= 0:
        return False

    return (number & (number - 1)) == 0


print(f"Is 8 power of 2 :  {isPowerOfTwo(8)}")
