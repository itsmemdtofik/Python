class FirstUniqueChar:

    @staticmethod
    def unique_char(s: str) -> int:
        if s is None or len(s) < 0:
            return -1

        char_map = {}
        for i in range(len(s)):
            char_map[s[i]] = char_map.get(s[i], 0) + 1

        for i in range(len(s)):
            if char_map[s[i]] == 1:
                return i

        return -1

    @staticmethod
    def first_uniq_char(s: str) -> int:
        freq = [0] * 26
        chars = list(s)

        for c in chars:
            freq[ord(c) - ord('a')] += 1

        for i in range(len(chars)):
            if freq[ord(chars[i]) - ord('a')] == 1:
                return i

        return -1


# Test cases
if __name__ == '__main__':
    print(FirstUniqueChar.first_uniq_char("leetcode"))  # Expected: 0
    print(FirstUniqueChar.first_uniq_char("loveleetcode"))  # Expected: 2
    print(FirstUniqueChar.first_uniq_char("aabb"))  # Expected: -1
    print(FirstUniqueChar.first_uniq_char(""))  # Expected: -1
