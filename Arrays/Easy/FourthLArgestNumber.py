"""
     * !Fourth-Largest Number
     * !Time Complexity: O(n), Space Complexity: O(1)
     * Find the fourth-largest number in array
     * !Approach:
     * Step1: Traverse the array
     * Step2: Store the fourth = third, third = second, second = first, first = arr[i]
     * Step3: Return the fourth largest
"""


def fourthLargestNumber(nums):
    if not nums or len(nums) < 4:
        return nums  # Not enough unique numbers

    # Remove duplicates to ensure distinct elements
    unique_nums = list(set(nums))

    # Initialize top 4
    first_largest = second_largest = third_largest = fourth_largest = float('-inf')

    for num in unique_nums:
        if num > first_largest:
            fourth_largest = third_largest
            third_largest = second_largest
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            fourth_largest = third_largest
            third_largest = second_largest
            second_largest = num
        elif num > third_largest:
            fourth_largest = third_largest
            third_largest = num
        elif num > fourth_largest:
            fourth_largest = num

    return fourth_largest


arr = [10, 20, 40, 30, 50, 50, 30]
print(f"Fourth largest element is: {fourthLargestNumber(arr)}")
