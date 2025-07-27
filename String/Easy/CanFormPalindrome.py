"""
     * <pre>
     * ! Check if a string's character can be re-arranged to form a palindrome.
     * A palindrome can have at most one character with an odd frequency (for odd-length strings)
     * All others must appear an even number of times.
     * Example: "add" -> true (can be re-arranged to dad)
     * Example: "bangalore" -> false (can not be re-arranged)
     * </pre>

"""


def canFormPalindrome(s):
    freq_map = {}
    for ch in s:
        freq_map[ch] = freq_map.get(ch, 0) + 1

    oddCount = 0
    for count in freq_map.values():
        if count % 2 != 0:
            oddCount += 1
            if oddCount > 1:
                return False
    return True


print(canFormPalindrome("racecar"))  # True
print(canFormPalindrome("aabb"))  # True
print(canFormPalindrome("abc"))  # False
