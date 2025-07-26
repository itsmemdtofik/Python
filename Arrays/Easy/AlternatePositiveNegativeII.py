def UsingStack(nums):
    if not nums or len(nums) < 2:
        return nums

    positive_stack = []
    negative_stack = []

    # Push the elements to stacks (reverse order like Java)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] >= 0:
            positive_stack.append(nums[i])
        else:
            negative_stack.append(nums[i])

    merge_index = 0
    result = [0] * len(nums)
    turn_position = True

    while positive_stack and negative_stack:
        if turn_position:
            result[merge_index] = positive_stack.pop()
        else:
            result[merge_index] = negative_stack.pop()
        merge_index += 1
        turn_position = not turn_position
    # Append remaining elements
    while positive_stack:
        result[merge_index] = positive_stack.pop()
        merge_index += 1
    while negative_stack:
        result[merge_index] = negative_stack.pop()
    return result


print(UsingStack([4, -3, -2, 7, -1, 5]))
# Output: [4, -3, 7, -2, 5, -1]
