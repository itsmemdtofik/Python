"""
     * <pre>
     * ! Largest Word Matcher
     * * Step1: Create a frequency map for input string
     * * Step2: Create a frequency map for word and check the if it can form the word
     * * Step3: Track the longest words that can be formed.
     *
     * ! Example Walkthrough
     * Dictionary: {"to", "banana", "toe", "dogs", "ababcd", "elephant"}
     * Input: "eot"
     *
     * Input frequency map: {e: 1, o: 1, t: 1}
     * Check each word:
     * "to" → {t: 1, o: 1} ✅ Can form.
     * "toe" → {t: 1, o: 1, e: 1} ✅ Can form.
     * "banana" → {b: 1, a: 3, n: 2} ❌ Cannot form.
     * "dogs" → {d: 1, o: 1, g: 1, s: 1} ❌ Cannot form.
     * "ababcd" → {a: 2, b: 2, c: 1, d: 1} ❌ Cannot form.
     * "elephant" → {e: 2, l: 1, p: 1, h: 1, a: 1, n: 1, t: 1} ❌ Cannot form.
     * Result: "toe" is the longest word that can be formed.
     * </pre>
"""

from typing import List, Set, Dict
from collections import defaultdict


def create_frequency_map(s: str) -> Dict[str, int]:
    frequency_map = defaultdict(int)
    if s is None:
        return frequency_map
    for c in s:
        frequency_map[c] += 1
    return frequency_map


def can_form_word(word: str, input_frequency_map: Dict[str, int]) -> bool:
    if word is None or input_frequency_map is None:
        return False
    word_frequency_map = create_frequency_map(word)

    for c, count in word_frequency_map.items():
        if input_frequency_map.get(c, 0) < count:
            return False
    return True


def find_largest_words(dictionary: Set[str], input_str: str) -> List[str]:
    result = []
    if dictionary is None or input_str is None:
        return result

    max_length = 0
    input_frequency_map = create_frequency_map(input_str)

    for word in dictionary:
        if can_form_word(word, input_frequency_map):
            if len(word) > max_length:
                max_length = len(word)
                result.clear()  # Clear previous shorter words
                result.append(word)
            elif len(word) == max_length:
                result.append(word)  # Add word of same max length

    return result


if __name__ == "__main__":
    dictionary = {"to", "banana", "toe", "dogs", "ababcd", "elephant"}

    input1 = "eot"
    result1 = find_largest_words(dictionary, input1)
    print(f"Input: {input1}, Output: {result1}")

    input2 = "ogtdes"
    result2 = find_largest_words(dictionary, input2)
    print(f"Input: {input2}, Output: {result2}")
