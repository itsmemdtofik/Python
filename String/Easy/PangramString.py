"""
     * <pre>
     * !Pangram: Check if given String is Pangram or not
     * A pangram (or holoalphabetic sentence) is a sentence that contains every
     * letter of the alphabet at least once.
     *
     * !Example:
     * 1. "The quick brown fox jumps over the lazy dog" is a pangram because it
     * contains all 26 letters of the English alphabet, from 'a' to 'z'.
     * 2. "Pack my box with five dozen liquor jugs" is another example of a pangram.
     * !Note: A pangram can be of any length, but it must include all 26 letters of the alphabet.
     * </pre>

"""

import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def find_missing_characters(sentence: str) -> str:
    sentence = sentence.lower()
    if not sentence:
        return ALPHABET

    # Remove non-alphabet characters
    cleaned_sentence = re.sub(r'[^a-z]', '', sentence)

    sentence_set = set(cleaned_sentence)

    missing_chars = []
    for char in ALPHABET:
        if char not in sentence_set:
            missing_chars.append(char)

    return ''.join(missing_chars)


if __name__ == "__main__":
    print(find_missing_characters("The quic brown for jumps over the lazy dog"))  # "k,x"
    print(find_missing_characters(""))  # full alphabet
    print(find_missing_characters("The quick brown fox jumps over the lazy dog"))  # ""
    print(find_missing_characters("Pack my box with five dozen liquor jugs"))  # ""
    print(find_missing_characters("Waltz, nymph, for quick jigs vex Bud."))  # ""
    print(find_missing_characters("Sphinx of black quartz, judge my vow."))  # ""
