def fourthSmallestNumber(nums):
    if not nums or len(nums) < 4:
        return None  # Not enough unique elements

    # Get unique numbers to remove duplicates
    unique_nums = list(set(nums))

    # Initialize the smallest values
    first = second = third = fourth = float('inf')

    for num in unique_nums:
        if num < first:
            fourth = third
            third = second
            second = first
            first = num
        elif num < second:
            fourth = third
            third = second
            second = num
        elif num < third:
            fourth = third
            third = num
        elif num < fourth:
            fourth = num

    return fourth


# Example usage
arr = [10, 20, 40, 30, 50, 50, 30]
print(f"Fourth smallest element is: {fourthSmallestNumber(arr)}")
