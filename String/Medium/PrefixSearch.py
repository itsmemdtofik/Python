"""
     * <pre>
     * !Prefix Search
     *
     * Provide an implementation of the findAll() method to in MyPrefixSearch.
     * Describing any trade-off arising from your implementation.
     * findAll() -> Returns a list of all location in a document where the
     * (case-insensitive)
     * words begins with the given prefix.
     *
     * *Example: Given the document = "a aa Aaa abca bca"
     *
     * 1. findAll("a") -> [0, 2, 5, 6]
     * 2. findAll("bc") -> [14]
     * 3. findAll(aA) -> [2, 5]
     * 4. findAll(abc) -> [9]
     *
     * Time complexity:
     * split("\\+s") -> O(n)
     * word.toLowerCase().startsWith(prefix.toLowerCase()) -> O(m)
     *
     * Over All : O(w * m)
     * </pre>
"""


class PrefixSearch:
    def __init__(self, document: str):
        self.document = document

    def find_all(self, prefix: str) -> list[int]:
        result = []

        if not prefix or not self.document:
            return result  # Return empty list for invalid input

        document = self.document.strip()
        words = document.split(" ")

        position = 0  # Tracks the starting position of each word
        for word in words:
            # Case-insensitive prefix check
            if word.lower().startswith(prefix.lower()):
                result.append(position)
            # Update position (word length + space)
            position += len(word) + 1

        return result


if __name__ == "__main__":
    search = PrefixSearch("a aa Aaa abca bca ")
    print(search.find_all("a"))  # Output: [0, 2, 5, 10]
    print(search.find_all("bc"))  # Output: [14]
    print(search.find_all("aA"))  # Output: [2, 5]
    print(search.find_all("abc"))  # Output: [9]
