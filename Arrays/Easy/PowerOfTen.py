"""
	* !Power of Base:
	* Given an integer n, return true if it is a power of three. Otherwise, return false.
	* An integer n is a power of three, if there exists an integer x such that n == 3x.
	* Example 1:
	* Input: n = 27
	* Output: true
	* Explanation: 27 = 3
	*
	* Example 2:
	* Input: n = 0
	* Output: false
	* Explanation: There is no x where 3x = 0.
	*
	* Example 3:
	* Input: n = -1
	* Output: false
	* Explanation: There is no x where 3x = (-1).
"""


def isPowerOfBase(number, base):
    if number is None or number <= 0 or base <= 1:
        return False

    while number % base == 0:
        number /= base
    return number == 1


num: int = 625
bas: int = 5
print(f"Is power of {num} and {bas} == {isPowerOfBase(num, bas)}")
