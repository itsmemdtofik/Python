"""
     * <pre>
     * !Snow Pack or Trapping rain water.
     *
     * Given an array of non-negative integers representing the elevations from the
     * vertical cross-section of the range of hills, determine how many units of
     * snow could be captured between the hills.
     *
     * For example: ({0, 1, 3}, {0, 1, 2},{0, 4, 2},{0, 3, 0})
     * Implement: Find the amount of snow that could be captured.
     * </pre>
"""


def trappingRainWater(height: list[int]) -> int:
    leftHeight = 0
    rightHeight = len(height) - 1
    leftMax = rightMax = snow = 0

    while leftHeight < rightHeight:
        if height[leftHeight] < height[rightHeight]:
            if height[leftHeight] >= leftMax:
                leftMax = height[leftHeight]
            else:
                snow = snow + leftMax - height[leftHeight]
            leftHeight += 1
        else:
            if height[rightHeight] >= rightMax:
                rightMax = height[rightHeight]
            else:
                snow = snow + rightMax - height[rightHeight]
            rightHeight -= 1
    return snow


nums: list[int] = [0, 1, 3, 0, 1, 2, 0, 4, 2, 0, 3, 0]
print(f"Collected Snow is: {trappingRainWater(nums)}")
