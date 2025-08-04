def getRemovalDuplicateStringUsingHashSet(s: str) -> str:
    seen = set()
    result = []

    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


print(getRemovalDuplicateStringUsingHashSet("hello"))  # "helo"
print(getRemovalDuplicateStringUsingHashSet("apple"))  # "aple"
print(getRemovalDuplicateStringUsingHashSet("mississippi"))  # "misp"
print(getRemovalDuplicateStringUsingHashSet("abc"))  # "abc" (no duplicates)
