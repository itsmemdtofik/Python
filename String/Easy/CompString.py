# -------------------------------------------------------
# Comparison of Strings : Three methods are used
# (1) Using manual compareTo equivalent
# (2) Using equals()
# (3) Using equalsIgnoreCase()
# -------------------------------------------------------

def compare_strings(str1, str2):
    # Manual compareTo logic
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i] != str2[i]:
            diff = ord(str1[i]) - ord(str2[i])
            return diff
    # If all characters same till min length, then difference of lengths
    return len(str1) - len(str2)

def equals(str1, str2):
    return str1 == str2

def equals_ignore_case(str1, str2):
    # Manual lowercase conversion
    def to_lowercase(s):
        res = ''
        for ch in s:
            if 'A' <= ch <= 'Z':
                res += chr(ord(ch) + 32)
            else:
                res += ch
        return res

    return to_lowercase(str1) == to_lowercase(str2)

def main():
    print("-------------------------------------------------------")
    str1 = "this is java programming"
    str2 = "This is java programming"
    
    # 1. Manual compareTo
    d = compare_strings(str1, str2)
    print(f"The difference between first string and second string is = {d}")

    # 2. equals
    bool_equal = equals(str1, str2)
    print("-------------------------------------------------------")
    print(f"This is = {bool_equal}")
    print("-------------------------------------------------------")

    # 3. equalsIgnoreCase
    bool_ignore_case = equals_ignore_case(str1, str2)
    print(f"This is = {bool_ignore_case}")
    print("-------------------------------------------------------")

if __name__ == "__main__":
    main()
