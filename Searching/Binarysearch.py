
#! Binary Search in Python
'''
#? Key Points:
Binary search requires the input array to be sorted.
The algorithm works by repeatedly dividing the search interval in half.
Time complexity is O(log n), which is much more efficient than linear search (O(n)) for large datasets.
Space complexity is O(1) as it uses constant space.
'''

def binarySearch(arr, target):
    """
    Perform binary search on a sorted array to find the target value.
    
    Args:
        arr: A sorted list of elements
        target: The value to search for
        
    Returns:
        The index of the target if found, otherwise -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
    
    return -1

def binarySearchRecursive(arr, target, left=0, right=None):
    """
    Perform binary search recursively on a sorted array.
    
    Args:
        arr: Sorted list of elements
        target: Value to search for
        left: Starting index (default 0)
        right: Ending index (default len(arr) - 1)
        
    Returns:
        Index of the target if found, otherwise -1
    """
    if right is None:
        right = len(arr) - 1  # Initialize right on first call
    
    if left > right:
        return -1  # Base case: target not found
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid  # Base case: target found
    elif arr[mid] < target:
        return binarySearchRecursive(arr, target, mid + 1, right)  # Search right half
    else:
        return binarySearchRecursive(arr, target, left, mid - 1)  # Search left half

# Example usage
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    
    result = binarySearchRecursive(sorted_list, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")

# Example usage:
if __name__ == "__main__":#it controls what part of your code runs automatically when you execute the file.
    sorted_list = [1, 3, 5, 7, 9, 11, 13]
    target = 1
    
    result = binarySearch(sorted_list, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the list")