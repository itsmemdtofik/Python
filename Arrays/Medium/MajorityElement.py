'''
 * ! Majority Element II - An element that occure [arr.length / 3] times.
 * 
 * Given an array arr[] consisting of n integers, the task is to find all the
 * array elements which occurs more than floor(n/3) times.
 * Note: The returned array of majority elements should be sorted.
 * 
 * Examples:
 * 
 * Input: arr[] = {2, 2, 3, 1, 3, 2, 1, 1}
 * Output: {1, 2}
 * Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3
 * = 2).
 * 
 * 
 * Input: arr[] = {-5, 3, -5}
 * Output: {-5}
 * Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 =
 * 1).
 * 
 * 
 * Input: arr[] = {3, 2, 2, 4, 1, 4}
 * Output: { }
 * Explanation: There is no majority element.
 * 
 * 
 '''

# Python3 program to find Majority
# element in an array using nested loops

# Function to find the Majority element in an array
# Python3 program to find Majority
# element in an array using nested loops

# Function to find the Majority element in an array
def majorityElement(arr):
    n = len(arr)  

    # Loop to consider each element as a candidate for majority
    for i in range(n):
        count = 0

        # Inner loop to count the frequency of arr[i]
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        # Check if count of arr[i] is more than half the size of the array
        if count > n // 2:
            return arr[i]

    # If no majority element found, return -1
    return -1

if __name__ == "__main__":
	arr = [1, 1, 2, 1, 3, 5, 1]
	print(majorityElement(arr))