from collections import OrderedDict


class IntegerToRoman:

    @staticmethod
    def int_to_roman(num: int) -> str:
        roman_map = OrderedDict()
        roman_map[1000] = "M"
        roman_map[900] = "CM"
        roman_map[500] = "D"
        roman_map[400] = "CD"
        roman_map[100] = "C"
        roman_map[90] = "XC"
        roman_map[50] = "L"
        roman_map[40] = "XL"
        roman_map[10] = "X"
        roman_map[9] = "IX"
        roman_map[5] = "V"
        roman_map[4] = "IV"
        roman_map[1] = "I"

        result = []
        for value, symbol in roman_map.items():
            while num >= value:
                result.append(symbol)
                num -= value

        return ''.join(result)


if __name__ == '__main__':
    print("Integer 58:", IntegerToRoman.int_to_roman(58))  # Output: LVIII
