"""
     * <pre>
     * !Longest Common Prefix using Sorting
     * The first string strs[0] is used as the starting point for comparison with all other strings in the array.
     *
     * ! How?
     * strs[i].indexOf(prefix) != 0 checks if prefix is not a prefix of strs[i].
     * If not, the prefix is shortened by removing its last character (prefix.substring(0, prefix.length() - 1)).
     * If prefix becomes empty during this process, it means there is no common prefix, so the function returns "".
     * @return
     * </pre>
"""


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    str1 = ["flower", "flow", "flight"]
    str2 = ["dog", "racecar", "car"]
    print(longest_common_prefix(str1))  # Output: "fl"
    print(longest_common_prefix(str2))  # Output: ""
