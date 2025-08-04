from collections import defaultdict


def getCommonElementInArray(nums1: list[int], nums2: list[int]) -> list[int]:
    # Convert first list to a "set" (using dictionary for manual implementation)
    freq_map = defaultdict(int)

    for num in nums1:
        freq_map[num] = True  # Using dictionary to simulate set

    result_map = defaultdict(int)
    for num in nums2:
        if num in freq_map:
            result_map[num] = True
    return list(result_map.keys())


print(getCommonElementInArray([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
print(getCommonElementInArray([1, 1, 2], [2, 2, 3]))  # [2]
print(getCommonElementInArray([], [1, 2, 3]))  # []
