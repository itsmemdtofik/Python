# ! Remove duplicates from a sorted array.
# Given a sorted array arr[] of size n, the goal is to rearrange the array so
# that all distinct elements appear at the beginning in sorted order.
# Additionally, return the length of this distinct sorted subarray.
# Note: The elements after the distinct ones can be in any order and hold any
# value, as they don’t affect the result.

# Examples:
# Input: arr[] = [2, 2, 2, 2]
# Output: [2]
# Explanation: All elements are 2, so only keep one instance of 2.

# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

# Input: arr[] = [1, 2]
# Output: [1, 2]
# Explanation: No change as all elements are distinct.

def remove_duplicates(arr):
    """
    Remove duplicates from a sorted array.
    The function returns a new array with all distinct elements at the start.

    Parameters:
    arr (list): The sorted array of integers.

    Returns:
    list: The array containing distinct elements.
    """
    if not arr or len(arr) < 2:
        return arr

    temp = []
    for num in arr:
        if num not in temp:
            temp.append(num)

    return temp

def remove_duplicates_inplace(nums):
    """
    Remove duplicates from a sorted array in-place.
    The function returns the number of distinct elements and modifies the array.

    Parameters:
    nums (list): The sorted array of integers.

    Returns:
    int: The number of distinct elements.
    """
    if not nums or len(nums) < 2:
        return 0

    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j

def remove_duplicates_using_set(arr):
    """
    Remove duplicates from a sorted array using a set.
    The function returns an array with distinct elements.

    Parameters:
    arr (list): The sorted array of integers.

    Returns:
    list: The array containing distinct elements.
    """
    if not arr or len(arr) < 2:
        return arr

    distinct_elements = set(arr)
    return list(distinct_elements)

def remove_duplicates_using_list(arr):
    """
    Remove duplicates from a sorted array using a list.
    The function returns an array with distinct elements.

    Parameters:
    arr (list): The sorted array of integers.

    Returns:
    list: The array containing distinct elements.
    """
    if not arr or len(arr) < 2:
        return arr

    result = []
    for num in arr:
        if num not in result:
            result.append(num)

    return result

def main():
    arr1 = [2, 2, 2, 2]
    arr2 = [1, 1, 2]
    arr3 = [1, 1, 2]

    print("After removing duplicates:", remove_duplicates(arr1))
    print("Using set:", remove_duplicates_using_set(arr2))
    print("Using list:", remove_duplicates_using_list(arr2))

    distinct_length = remove_duplicates_inplace(arr3)
    print("In-place distinct elements:", arr3[:distinct_length])

if __name__ == "__main__":
    main()
