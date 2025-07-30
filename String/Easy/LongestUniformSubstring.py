def repeated_substring(s: str) -> list[int]:
    if not s:
        return [-1, 0]

    max_start = 0
    max_length = 1
    current_start = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            if i - current_start + 1 > max_length:
                max_length = i - current_start + 1
                max_start = current_start
        else:
            current_start = i

    return [max_start, max_length]


if __name__ == "__main__":
    # Test cases
    s1 = "10000111"
    s2 = "aabbbbbCdAA"
    s3 = "abbbccda"

    # Print the results
    print(f'For input "{s1}", the longest uniform substring is at index: {repeated_substring(s1)}')
    print(f'For input "{s2}", the longest uniform substring is at index: {repeated_substring(s2)}')
    print(f'For input "{s3}", the longest uniform substring is at index: {repeated_substring(s3)}')
