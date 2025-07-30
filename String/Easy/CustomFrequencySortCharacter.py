"""
     * <pre>
     * ! Custome Frequency Sort Of Character
     * Sort characters in a string by their frequency in descending order or ascending order.
     * Maintain the order of first appearance for ties.
     * Example: "tree" -> "eert" OR "eetr"
     * </pre>
"""
from collections import defaultdict


def custom_frequency_sort_of_character(s: str) -> str:
    if not s:
        return ""

    # Count character frequencies
    freq_map = defaultdict(int)
    for ch in s:
        freq_map[ch] += 1

    # Sort characters by frequency (descending), maintaining insertion order for ties
    sorted_chars = sorted(freq_map.keys(), key=lambda x: -freq_map[x])

    # Build the result string
    result = []
    for ch in sorted_chars:
        result.append(ch * freq_map[ch])

    return ''.join(result)


if __name__ == "__main__":
    print(custom_frequency_sort_of_character("tree"))  # Output: "eetr" or "eert"
