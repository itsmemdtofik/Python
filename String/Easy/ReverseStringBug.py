"""
     * <pre>
     * ! Reverse String Bug
     *
     * Example 1: reverse the character
     * Input: s = ["h","e","l","l","o"]
     * Output: ["o","l","l","e","h"]
     *
     * Example 2: (reverse the words of string )
     * Input: s = "the sky is blue"
     * Output: "blue is sky the"
     *
     * Example 3: Reverse the entire string
     * Input: "abcdefgh"
     * ouput: "hgfedcba"
     *
     * </pre>
"""


def reverse_character(arr: list[str]) -> str:
    left = 0
    right = len(arr) - 1

    # Reverse the character array in place
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Build the output with double quotes
    return ",".join(f'"{char}"' for char in arr)


def reverse_words_of_string(s: str) -> str:
    # Remove leading/trailing spaces and split by one or more spaces
    words = s.strip().split()

    # Reverse the words and join with single spaces
    return " ".join(reversed(words))


def reverse_string(s: str) -> str:
    s = s.strip()
    return s[::-1]  # Pythonic way to reverse string


if __name__ == "__main__":
    print(reverse_character(['h', 'e', 'l', 'l', 'o']))  # "o","l","l","e","h"
    print("Reverses words are:", reverse_words_of_string(" the sky is blue"))  # blue is sky the
    print("Reverse String is:", reverse_string("abcdefgh"))  # hgfedcba
