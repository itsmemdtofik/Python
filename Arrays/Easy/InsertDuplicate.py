# 
# * Insert duplicate of K adjacent to it for its every occurrence in array.
# 
# Given an array arr consisting of N integers and an integer K, the task is to
# insert an adjacent K for every occurrence of it in the original sequence and
# then truncate the array to the original length using an O(1) auxiliary space.
# 
# Examples:
# 
# Input: arr[] = {1, 0, 2, 3, 0, 4, 5, 0}, K = 0
# Output: {1, 0, 0, 2, 3, 0, 0, 4}
# Explanation:
# The given array {1, 0, 2, 3, 0, 4, 5, 0} is modified to {1, 0, 0, 2, 3, 0, 0, 4}
# after insertion of two 0’s and truncation of extra elements.
# 
# Input: arr[] = {7, 5, 8}, K = 8
# Output: {7, 5, 8}
# Explanation:
# After inserting an adjacent 8 into the array, it got truncated to restore the
# original size of the array.
# 

class InsertDuplicateElement:

    @staticmethod
    def insertDuplicate(nums, K):
        if nums is None or len(nums) == 0 or len(nums) < 2:
            return nums
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == K:
                count += 1

        n = len(nums) + count
        newarr = [0] * n
        j = 0

        for i in range(len(nums)):
            newarr[j] = nums[i]
            j += 1
            if nums[i] == K:
                newarr[j] = K
                j += 1

        return newarr

    @staticmethod
    def main():
        arr1 = [7, 5, 8]
        K1 = 8

        arr2 = [1, 0, 2, 3, 0, 4, 5, 0]
        K2 = 0

        m = InsertDuplicateElement.insertDuplicate(arr1, K1)
        print("Elements are: ", end="")
        for i in range(len(arr1)):
            print(m[i], end=", ")
        print()

        n = InsertDuplicateElement.insertDuplicate(arr2, K2)
        print("Elements are: ", end="")
        for i in range(len(arr2)):
            print(n[i], end=", ")
        print()

if __name__ == "__main__":
    InsertDuplicateElement.main()
