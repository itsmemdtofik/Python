def maximumOneRepetitive(nums):
    count = 0
    result = 0

    for num in nums:
        if num == 0:
            count = 0
        else:
            count += 1
            result = max(result, count)
    return result


number = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
print(f"Maximum Repetitive One is: {maximumOneRepetitive(number)}")
