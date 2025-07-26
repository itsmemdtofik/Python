"""
     * <pre>
     * !Count Length Of Cycle: Floyd's Tortoise and Hare algorithm (Cycle-Finding Algorithm)
     * !Time Complexity: O(n), Space Complexity: O(1)
     * Step1: Tortoise (slow) moves 1 step at a time.
     * Step2: Hare (fast) moves 2 steps at a time.
     * Step3: If they meet(slow == fast), a cycle exists.
     * Step4: To find cycle length, freeze fast and move slow until they meet again, counting steps.
     * Step5: Return the cycle length
     * </pre>
"""
def countLengthOfCycle(nums, start_index):

    if not nums or start_index < 0 or start_index >= len(nums):
        return -1

    slow = start_index
    fast = start_index

    while 0 <= fast < len(nums):
        slow = nums[slow]
        fast = nums[fast]

        if fast < 0 or fast >= len(nums):
            break
        fast = nums[fast]

        if slow == fast:
            cycle_len = 0
            while True:
                slow = nums[slow]
                cycle_len += 1
                if slow == fast:
                    break
            return cycle_len
    return -1

arr = [1, 2, 3, 4, 2]
print(countLengthOfCycle(arr, 0))  # Output: 3 (cycle: 2 → 3 → 4 → 2)

