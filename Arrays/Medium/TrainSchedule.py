"""
     * <pre>
     * ! Train Schedule : Two Pointer + TreeMap Approach
     * Given arrival and departure times of trains, determine the minimum number of platforms needed so no trains waits.
     * Arrival = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
     * Departure = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
     * Output = 3
     * Explanation: Max 3 trains are at the station at the same time between 9:40 and 12:00
     * When a train arrives → we need one more platform (+1)
     * When a train departs → we can free one platform (-1)
     * We store these changes using a TreeMap, which keeps time sorted automatically.
     * 900  → +1
     * 910  → -1
     * 940  → +1
     * 950  → +1
     * 1100 → +1
     * 1120 → -1
     * 1130 → -1
     * 1200 → -1
     * 1500 → +1
     * 1800 → +1
     * 1900 → -1
     * 2000 → -1
     * Processed chronologically, the algorithm finds the peak overlap = 3 platforms.
     * </pre>
"""
from collections import defaultdict
from typing import List


class TrainSchedule:

    @staticmethod
    def findPlatform(arrival: List[int], departure: List[int]) -> int:

        arrival.sort()
        departure.sort()

        platform = 1
        maxPlatform = 1

        i = 1
        j = 0

        while i < len(arrival) and j < len(departure):
            if arrival[i] <= departure[j]:
                platform += 1
                i += 1
            else:
                platform -= 1
                j += 1
            maxPlatform = max(maxPlatform, platform)

        return maxPlatform

    @staticmethod
    def findPlatformII(arrival: List[int], departure: List[int]) -> int:

        treeMap = defaultdict(int)

        for time in arrival:
            treeMap[time] += 1

        for time in departure:
            treeMap[time] -= 1

        platform = 0
        maxPlatform = 0

        for time in sorted(treeMap):
            platform += treeMap[time]
            maxPlatform = max(maxPlatform, platform)

        return maxPlatform


# Example usage
if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dept = [910, 1200, 1120, 1130, 1900, 2000]

    print("Using TreeMap-like logic:", TrainSchedule.findPlatform(arr, dept))  # Output: 3
    print("Using two-pointer logic:", TrainSchedule.findPlatformII(arr, dept))
