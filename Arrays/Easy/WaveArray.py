# **************************
# Wave Array
# **************************

# Sort an array in wave form.
# Given an unsorted array of integers, sort the array into a wave array. 
# An array arr[0..n-1] is sorted in wave form if:
# arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

# Examples:

# Input: arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
# Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80}
# Explanation: The array is sorted in a wave form as: 
# {10, 5, 6, 2, 20, 3, 100, 80}

# Input: arr[] = {20, 10, 8, 6, 4, 2}
# Output: arr[] = {20, 8, 10, 4, 6, 2}
# Explanation: The array is sorted in a wave form as:
# {20, 8, 10, 4, 6, 2}

# Python function to sort the array arr[0..n-1] in wave form,
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
# Python function to sort the array arr[0..n-1] in wave form,
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]


def sortInWave(arr, n):

    # Traverse all even elements
    for i in range(0, n , 2):

        # If current even element is smaller than previous
        if (i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]

        # If current even element is smaller than next
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]


arr = [10, 5, 6, 3, 2, 20, 100, 80]
sortInWave(arr, len(arr))
for i in range(0, len(arr)):
    print(arr[i])
