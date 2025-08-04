from collections import defaultdict


def getFirstNonRepeatingCharacterUsingHashMap(s: str) -> str | None:
    freq_map = defaultdict(int)

    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    for char, value in freq_map.items():
        if value == 1:
            return char
    return None


def getFirstNonRepeatingCharacterUsingHashMapII(s: str) -> str:
    # Manual frequency count using dictionary
    freq_map = {}
    for char in s:
        if char in freq_map:
            freq_map[char] = freq_map[char] + 1
        else:
            freq_map[char] = 1

    # Check characters in original order
    for char in s:
        if freq_map[char] == 1:
            return char

    return '\0'  # Return null char if none found


# Optimized Version (Using OrderedDict)
def first_unique_char(s: str) -> str:  # If you want exact Java-like behavior with order preservation
    from collections import OrderedDict
    count = OrderedDict()
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char, freq in count.items():
        if freq == 1:
            return char
    return '\0'


print(getFirstNonRepeatingCharacterUsingHashMapII("alccohhalz"))

"""
Here's your **Key Comparison Table** in a clean and structured format:

| **Feature**              | **`{}` (dict)**    | **`defaultdict(int)`** | **`OrderedDict`**   |
| ------------------------ | ------------------ | ---------------------- | ------------------- |
| **Missing Key Handling** | `KeyError`         | Auto-initializes       | `KeyError`          |
| **Insertion Order**      | Preserved (Py3.7+) | Preserved (Py3.7+)     | Always Preserved    |
| **Typical Use Case**     | General purpose    | Frequency counting     | Need strict order   |
| **Counting Code**        | Manual checks      | Clean `+= 1`           | `.get(char, 0) + 1` |
| **Memory Usage**         | Lowest             | Slightly higher        | Highest             |

"""
