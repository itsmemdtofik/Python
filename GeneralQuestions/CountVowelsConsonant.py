def getCountVowelsConsonant(s: str) -> tuple[int, int]:
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in {'a', 'e', 'i', 'o', 'u'}:
                v += 1
            else:
                c += 1
    return v, c


# Vowel/Consonant Tests
print(getCountVowelsConsonant("Hello World"))  # (3, 7)
print(getCountVowelsConsonant("Python"))  # (1, 5)
print(getCountVowelsConsonant("AEiou"))  # (5, 0)


def count_vowels_consonants_enhanced(s: str) -> tuple[int, int]:
    letters = [c.lower() for c in s if c.isalpha()]
    vowels = sum(1 for c in letters if c in {'a', 'e', 'i', 'o', 'u'})
    return vowels, len(letters) - vowels


# Vowel/Consonant Tests
print(count_vowels_consonants_enhanced("Hello World"))  # (3, 7)
print(count_vowels_consonants_enhanced("Python"))  # (1, 5)
print(count_vowels_consonants_enhanced("AEiou"))  # (5, 0)
