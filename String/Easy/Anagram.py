"""
 * !Anagram String
 *
 * <pre>
 * A anagram string is a word or phrase formed by rearranging the lettters of a different words typically using the original words.
 * Example : "listen" and "silent" are anagram because we can rearrange the "listen" to form "silent"
 * Example : "triangle" and "integral" are also anagrams because we can rearrange the "triangle" to form "integral"
 * Example : "hello" and "world" are not anagrams because we can not form the words "world" from "hello"
 * </pre>

"""


class Anagram:

    @staticmethod
    def anagram_hashmap(s1: str, s2: str) -> bool:
        # Convert to lowercase
        s1 = s1.lower()
        s2 = s2.lower()

        if len(s1) != len(s2):
            return False

        # Step1: Count frequency of each character in str1
        freq_map = {}
        for char in s1:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Step2: Decrease frequency using str2
        for char in s2:
            if char not in freq_map or freq_map[char] == 0:
                return False
            freq_map[char] -= 1

        return True

    @staticmethod
    def is_anagram(str1: str, str2: str) -> bool:
        str1 = str1.lower()
        str2 = str2.lower()

        if len(str1) != len(str2):
            return False

        count = [0] * 256  # Assuming extended ASCII

        for char in str1:
            count[ord(char)] += 1

        for char in str2:
            if count[ord(char)] == 0:
                return False
            count[ord(char)] -= 1

        return True


if __name__ == '__main__':
    print("Are 'listen' and 'silent' anagrams?", Anagram.is_anagram("listen", "silent"))
    print("Are 'evil' and 'vile' anagrams?", Anagram.is_anagram("evil", "vile"))
    print("Are 'triangle' and 'integral' anagrams?", Anagram.is_anagram("triangle", "integral"))
    print("Are 'hello' and 'world' anagrams?", Anagram.is_anagram("hello", "world"))
    print("Are 'dusty' and 'study' anagrams?", Anagram.is_anagram("dusty", "study"))
