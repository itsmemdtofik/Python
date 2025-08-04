def getAllSubstring(s: str):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(s[i:j])


print("Using Slicing:")
getAllSubstring("abc")


def getSubstringUsingNestedLoop(s: str) -> None:
    n = len(s)

    for i in range(n):
        for j in range(i, n):

            # Manually build substring character by character
            substring = []
            for k in range(i, j + 1):
                substring.append(s[k])
            print(''.join(substring))  # Combine character into a string


if __name__ == '__main__':
    print("Using Nested Loop:")
    getSubstringUsingNestedLoop("abc")
