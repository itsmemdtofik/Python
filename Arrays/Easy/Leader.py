# 
# * Leaders in an Array;
# 
# Given an array arr[] of size n, the task is to find all the Leaders in the array.
# An element is a Leader if it is greater than or equal to all the elements to its right side.
# Note: The rightmost element is always a leader.
# 
# Examples
# 
# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2] 
# Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2]
# therefore 17 is a leader. 5 is greater than all the elements to its right i.e. [2],
# therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
# 
# Input: arr[] = [1, 2, 3, 4, 5, 2]
# Output: [5, 2]
# Explanation: 5 is greater than all the elements to its right i.e., [2],
# therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
# 
# ? Approach:
# 
# Step1: Start from the end(rightmost element), which is always a leader.
# Step2: Traverse the array from right to left, compare each element with the leader.
# Step3: If an element is greater than or equal to leader, it is leader and we update the leader.
# Step4: Stores the leader in list(Since we are processing from right to left, we will reverse result list at the end).
# The final list of leaders will be in reverse order, so reverse it before returning.
#

class LeaderInArray:

    @staticmethod
    def leaderInArr(nums):
        leader = nums[-1]
        result = []
        result.append(leader)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= leader:
                result.append(nums[i])
                leader = nums[i]

        result.reverse()
        return result

    @staticmethod
    def main():
        arr1 = [1, 2, 3, 4, 5, 2]
        print("Leaders in array 1:", LeaderInArray.leaderInArr(arr1))

        arr2 = [16, 17, 4, 3, 5, 2]
        print("Leaders in array 2:", LeaderInArray.leaderInArr(arr2))

if __name__ == "__main__":
    LeaderInArray.main()
