def roman_to_int(s: str) -> int:
    answer = 0
    number = 0

    # Dictionary mapping Roman numerals to their values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(s) - 1, -1, -1):
        number = roman_values[s[i]]

        if 4 * number < answer:
            answer -= number
        else:
            answer += number

    return answer


if __name__ == "__main__":
    print("Roman to Integer : (III) :", roman_to_int("III"))  # 3
    print("Roman to Integer : (LVIII) :", roman_to_int("LVIII"))  # 58
    print("Roman to Integer : (MCMXCIV) :", roman_to_int("MCMXCIV"))  # 1994
