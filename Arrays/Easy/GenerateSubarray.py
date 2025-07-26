"""
     * <pre>
     * !Generating All Subarrays
     *
     * !Approach1: Instead of using three nested loops (O(n³)), we can generate subarrays in O(n²) by:
     *
     * 1. Fixing a starting point i (outer loop).
     * 2. Expanding the subarray from i to j (inner loop), where j moves from i to n-1.
     * 3. Building the subarray incrementally (without recomputing from scratch each time).
     *
     * !Approach2: Using three nested loops O(n^3)
     *
     * </pre>
"""


def generateSubarrayUsingList(nums):
    subarrays = []
    for i in range(len(nums)):
        currentSubarray = []
        for j in range(i, len(nums)):
            currentSubarray.append(nums[j])  # Expand subarray
            subarrays.append(currentSubarray.copy())  # Store a copy
    return subarrays


def generateSubarrayUsingNestedLoop(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print("[", end="")
            for k in range(i, j + 1):
                print(f"{nums[k]}, ", end="")
            print("]")


arr = [1, 2, 3]

print("Generated Subarrays (Returned):")
all_subs = generateSubarrayUsingList(arr)
for sub in all_subs:
    print(sub)

print("\nPrinted Subarrays (Direct Print):")
generateSubarrayUsingNestedLoop(arr)
