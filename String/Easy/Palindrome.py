
#! Palindrom in Python

def isPalindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # If it's already a palindrome, return the original string
    if s == s[::-1]:
        return s
    
    # Generate the palindrome by appending the reverse (without the first character)
    palindrome = s + s[-2::-1]  # Exclude the first character of the reverse part
    
    return palindrome

# Test
print(isPalindrome("hello"))  # "hellolleh"
print(isPalindrome("A man, a plan, a canal, Panama"))  # Already a palindrome, returns as is


# Test
print(isPalindrome("A man, a plan, a canal, Panama"))  # True
print(isPalindrome("Was it a car or a cat I saw?"))    # True
print(isPalindrome("malayalam")) 
print(isPalindrome("mohammad tofik"))

def anotherPalindrome(string):
    string = ' '.join(char.lower() for char in string if char.isalnum())
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

print(anotherPalindrome("malayalam")) 