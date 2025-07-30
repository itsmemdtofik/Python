"""
     * <pre>
     * !The Magic Potion problem is a string compression challenge where: Greedy Run-Length Substring Compression
     * You replace repeated substrings with a special character (*).
     * The goal is to minimize the encoded string's length while keeping it reversible (if needed).
     *
     * !Example:
     * "ABABCABAB" → "AB*C*" (since "AB" repeats twice, then "ABAB" repeats once).
     * "ABCABC" → "ABC*" ("ABC" repeats once)
     * </pre>
"""


def magic_potion(s: str) -> int:
    if not s:
        return 0

    sb = [s[0]]
    count = 1
    i = 1

    while i < len(s):
        found_repeat = False

        # Check if the next 'i' chars match the first 'i' chars
        if i * 2 <= len(s):
            is_repeat = True
            for j in range(i):
                if s[j] != s[i + j]:
                    is_repeat = False
                    break
            if is_repeat:
                sb.append('*')
                count += 1
                i += i  # Skip the repeated part
                found_repeat = True

        if not found_repeat:
            sb.append(s[i])
            count += 1
            i += 1

    print(''.join(sb), end=' ')
    return count


if __name__ == "__main__":
    print("Minimal steps: [ABCABCE] :", magic_potion("ABCABCE"))
    print("Minimal steps: [ABABCABABCD] :", magic_potion("ABABCABABCD"))
    print("Minimal steps: [ABCDABCE] :", magic_potion("ABCDABCE"))
    print("Minimal steps: [ABABCABABCE] :", magic_potion("ABABCABABCE"))
