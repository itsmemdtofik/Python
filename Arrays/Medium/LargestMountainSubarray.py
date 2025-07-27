"""
     * <pre>
     * !Longest Mountain Subarray
     * Given a num say nums[] with N elements, the task is to find out the longest sub-num say
     * which has the shape of a mountain.
     *
     * @param Note: A mountain sub-num say starts with an increasing sequence,
     * reaches a peak, and then follows a decreasing sequence.
     *
     * Input: nums = [2, 2, 2]
     * Output: 0
     * Explanation: No sub-num say exists that shows the behavior of a mountain sub-num say.
     *
     * Input: nums = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]
     * Output: 11
     * Explanation: Longest sub-num say Mountain [1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5] which have length 11
     *
     * !Approach: Using the Nested loops - O(N^2) Time and O(1) Space
     * We can solve this problem using nested loops: the outer loop iterates over the num say,
     * while the inner loop finds the mountain length starting at the outer loop's index.
     * The inner loop first checks the increasing slope, then the decreasing slope.
     * If both exist, we update the maximum mountain length accordingly.
     * </pre>
"""
def find_longest_mountain(nums):
    n = len(nums)
    longest = 0
    i = 1

    while i < n - 1:
        # Check if nums[i] is a peak
        if nums[i - 1] < nums[i] > nums[i + 1]:
            left = i - 1
            right = i + 1

            # Expand to the left
            while left > 0 and nums[left - 1] < nums[left]:
                left -= 1

            # Expand to the right
            while right < n - 1 and nums[right] > nums[right + 1]:
                right += 1

            # Update the longest mountain length
            longest = max(longest, right - left + 1)

            # Move i to the end of this mountain
            i = right
        else:
            i += 1

    return longest


# Equivalent to Java main() method
if __name__ == "__main__":
    nums1 = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]
    print("Expected: 11 == ", find_longest_mountain(nums1))

    nums2 = [2, 2, 2]
    print("Expected: 0 == ", find_longest_mountain(nums2))
