
#! Second Smallest Number

def secondSmall(arr):
    if not arr or len(arr) < 2:
        return None
    
    first = second = float('inf')

    for num in arr:
        if num < first:
            second = first  # First store old first
            first = num     # Then update first
        elif num < second and num != first:  # Strictly between first and second
            second = num
    
    # Check if second was never updated
    if second == float('inf'):
        return None
    
    return second

arr = [1,11, 2, 2, 3, 4, 5]
print(secondSmall(arr))  # Output: 2

