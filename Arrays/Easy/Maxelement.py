
#! Find Maximum element in array

def findMaxElement(arr):
    if not arr or len(arr) < 2:
        return None

    first = float('-inf')
    for num in arr:
        if num > first:
            first = num

    if first == float('-inf'):
        return None
    return first


arr = [1,2,3,4]
print(findMaxElement(arr))