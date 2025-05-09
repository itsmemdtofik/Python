# ! Remove all occurrences of an element in an array.
# Given an integer array arr[] and an integer ele, the task is to remove all
# occurrences of ele from arr[] in-place and return the number of elements
# which are not equal to ele. If there are k elements which are not equal to ele,
# then the input array arr[] should be modified such that the first k elements contain
# the elements which are not equal to ele, and the remaining elements can be anything.

# Note: The order of first k elements may be changed.

# Example:

# Input: arr[] = [3, 2, 2, 3], ele = 3
# Output: 2
# Explanation: The answer is 2 because there are 2 elements which are not equal
# to 3, and arr[] will be modified such that the first 2 elements contain
# the elements which are not equal to 3, and the remaining elements can be any.
# So, modified arr[] = [2, 2, _, _]

# Input: arr[] = [0, 1, 3, 0, 2, 2, 4, 2], ele = 2
# Output: 5
# Explanation: The answer is 5 because there are 5 elements which are not equal
# to 2, and arr[] will be modified such that the first 5 elements contain
# the elements which are not equal to 2, and the remaining elements can be any.
# So, modified arr[] = [0, 1, 3, 0, 4, _, _, _]

def remove_all_occurrences(arr, element):
    """
    Remove all occurrences of the given element from the array in place.
    The function modifies the input array and returns the count of elements
    that are not equal to the given element.
    
    Parameters:
    arr (list): The list of integers.
    element (int): The element to be removed.
    
    Returns:
    int: The number of elements that are not equal to the given element.
    """
    if not arr:
        return 0
    
    count = 0
    for i in range(len(arr)):
        if arr[i] != element:
            arr[count] = arr[i]
            count += 1
    
    return count

def main():
    arr1 = [3, 2, 2, 3]
    element1 = 2
    arr2 = [0, 1, 3, 0, 2, 2, 4, 2]
    element2 = 2
    
    print("The answer is:", remove_all_occurrences(arr1, element1))
    print("The answer is:", remove_all_occurrences(arr2, element2))

if __name__ == "__main__":
    main()
