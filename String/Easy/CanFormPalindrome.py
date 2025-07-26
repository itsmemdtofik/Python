'''
A string can form a palindrome if:
At most one character has an odd frequency (in case of odd-length palindrome).
All characters have even frequencies (in case of even-length palindrome).
'''

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


def print(param):
    pass


print(canFormPalindrome("racecar"))   # True
print(canFormPalindrome("aabb"))      # True
print(canFormPalindrome("abc"))       # False
