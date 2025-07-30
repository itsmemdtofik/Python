"""
 * <pre>
 * !Distance between two strings.
 *
 * !There are two approaches:
 *
 * 1.Hamming Distacne:
 * Definition: The number of positions at which the corresponding characters
 * in the two strings are different. This method can only be applied to strings
 * of equal length.
 *
 * Example:
 * Strings: "karolin" and "kathrin"
 * Hamming Distance = 3 (The positions 3, 4, and 5 differ).
 *
 * !Levenshtein Distance:
 * Definition: The minimum number of insertions, deletions, or substitutions
 * required to convert one string into another.
 *
 * Example:
 * Strings: "kitten" and "sitting"
 * 1. Substitute 'k' -> 's' -> 1
 * 2. Substitute 'e' -> 'i' -> 1
 * 3. Add        'g' -> to the end -> 1
 * Result = 3.
 * Levenshtein Distance = 3 (substitute 'k' with 's', substitute 'e' with 'i', and append 'g').
 * <pre>
"""


class DistanceBetweenString:
    class HammingDistance:
        @staticmethod
        def findDistance(str1: str, str2: str) -> int:
            # Step 1: Check if strings are of equal length
            if len(str1) != len(str2):
                raise ValueError("Strings must be of equal length")

            # Step 2 & 3: Compare characters at each position
            distance = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    distance += 1

            # Step 4: Return mismatch count
            return distance

    class LevenshteinDistance:
        @staticmethod
        def findDistance(str1: str, str2: str) -> int:
            len1 = len(str1)
            len2 = len(str2)

            # Step 2: Initialize matrix
            dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

            # Step 3: Fill base cases
            for i in range(len1 + 1):
                dp[i][0] = i  # deletion
            for j in range(len2 + 1):
                dp[0][j] = j  # insertion

            # Step 4: Fill rest of matrix
            for i in range(1, len1 + 1):
                for j in range(1, len2 + 1):
                    cost = 0 if str1[i - 1] == str2[j - 1] else 1
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # deletion
                        dp[i][j - 1] + 1,  # insertion
                        dp[i - 1][j - 1] + cost  # substitution
                    )

            # Step 5: Return result
            return dp[len1][len2]


def main():
    str1 = "ab"
    str2 = "abc"

    try:
        result = DistanceBetweenString.LevenshteinDistance.findDistance(str1, str2)
        print("Levenshtein Distance:", result)
    except ValueError as e:
        print(e)

    str3 = "karolin"
    str4 = "kathrin"

    try:
        result = DistanceBetweenString.HammingDistance.findDistance(str3, str4)
        print("Hamming Distance:", result)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
