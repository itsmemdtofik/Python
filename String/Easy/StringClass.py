def remove_particular_character(string):
    string = string.lower()
    another_string = ""
    for ch in string:
        if ch == 'm':
            another_string = string.replace(ch, 'c')
    print("The string is", another_string)

def consonant_vowels(s):
    s = s.lower()
    count_consonant = 0
    count_vowels = 0
    for ch in s:
        if ch in 'aeiou':
            count_vowels += 1
        elif 'a' <= ch <= 'z':
            count_consonant += 1

    if count_consonant > 0:
        print("Consonants are:", count_consonant)
    if count_vowels > 0:
        print("Vowels are:", count_vowels)

def count_digit_space(s):
    s = s.lower()
    count_space = 0
    count_digit = 0
    for ch in s:
        if ch == ' ':
            count_space += 1
        elif '0' <= ch <= '9':
            count_digit += 1

    if count_space > 0:
        print("Spaces are:", count_space)
    if count_digit > 0:
        print("Digits are:", count_digit)

def count_frequency(s, ch):
    s = s.lower()
    return s.count(ch)

def remove_vowels(s):
    s = s.lower()
    for ch in s:
        if ch not in 'aeiou' and 'a' <= ch <= 'z':
            print(ch, end='')
    print()

def remove_consonant(s):
    s = s.lower()
    for ch in s:
        if ch in 'aeiou':
            print(ch, end='')
    print()

def frequency_of_each_character(s):
    s = s.lower()
    freq = {}
    for ch in s:
        if ch != ' ':
            freq[ch] = freq.get(ch, 0) + 1

    print("Character           :            Frequency")
    for ch, count in freq.items():
        print(f"{ch}                                  {count}")

def vowels_and_consonants_using_char_array(s):
    s = s.lower()
    vowels_count = 0
    consonant_count = 0
    print("The vowels are: ", end='')
    for ch in s:
        if ch in 'aeiou':
            print(ch, end=', ')
            vowels_count += 1
    print()

    print("The consonants are: ", end='')
    for ch in s:
        if ch not in 'aeiou' and 'a' <= ch <= 'z':
            print(ch, end=', ')
            consonant_count += 1
    print()

    if vowels_count > 0:
        print("The total number of vowels in the given string is:", vowels_count)
    if consonant_count > 0:
        print("The total number of consonants in the given string is:", consonant_count)

def check_vowel(ch):
    return ch in 'aeiou'

def vowels_and_consonants_using_array_list(s):
    s = s.lower()
    vowels = []
    consonants = []
    vowels_count = 0
    consonants_count = 0

    for ch in s:
        if 'a' <= ch <= 'z':
            if check_vowel(ch):
                vowels.append(ch)
                vowels_count += 1
            else:
                consonants.append(ch)
                consonants_count += 1

    print(f"The vowels are: {vowels} And count is: {vowels_count}")
    print()
    print(f"The consonants are: {consonants} And count is: {consonants_count}")
    print()

def reverse_string_using_recursion(s):
    if len(s) == 0 or len(s) == 1:
        print("The string is:", s)
        return

    print(s[-1])
    reverse_string_using_recursion(s[:-1])

def main():
    s = input("Enter the string: ")
    vowels_and_consonants_using_array_list(s)
    reverse_string_using_recursion(s)

if __name__ == "__main__":
    main()
