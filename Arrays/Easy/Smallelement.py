
#! Fid smallest element in an array

def findSmallElement(arr):
    if not arr or len(arr) < 2:
        return None
    
    small = float('inf')

    for num in arr:
        if num < small:
            small = num
    if small == float('inf'):
        return None
    return small

arr = [1,2,3,4,5, -100]
print(findSmallElement(arr))