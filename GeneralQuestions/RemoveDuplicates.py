def getDuplicateRemovalUsingHashSet(nums: list[int]) -> list[int]:
    seen = set()
    return [x for x in nums if not (x in seen or seen.add(x))]


print(f"Using HashSet:")
print(getDuplicateRemovalUsingHashSet([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(getDuplicateRemovalUsingHashSet([5, 5, 5, 5, 5]))  # [5]
print(getDuplicateRemovalUsingHashSet([]))  # []
print(getDuplicateRemovalUsingHashSet([1, 2, 3, 2, 1]))  # [1, 2, 3] (order preserved)


def getDuplicateRemovalUsingSorting(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    # First sort the array to bring duplicates together
    arr_sorted = sorted(arr)

    result = [arr_sorted[0]]

    # Iterate through the sorted array and skip duplicates
    for i in range(1, len(arr_sorted)):
        if arr_sorted[i] != arr_sorted[i - 1]:
            result.append(arr_sorted[i])

    return result


print(f"Using Sorting:")
print(getDuplicateRemovalUsingSorting([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(getDuplicateRemovalUsingSorting([5, 5, 5, 5, 5]))  # [5]
print(getDuplicateRemovalUsingSorting([]))  # []
print(getDuplicateRemovalUsingSorting([3, 1, 2, 2, 1]))  # [1, 2, 3] (sorted)


def getDuplicateRemovalUsingNestedLoop(arr: list[int]) -> list[int]:
    result = []
    n = len(arr)

    for i in range(n):
        # Check if this element already exists in result
        duplicate = False
        for j in range(len(result)):
            if arr[i] == result[j]:
                duplicate = True
                break

        # If not a duplicate, add to result
        if not duplicate:
            result.append(arr[i])

    return result


print(f"Using Nested Loop:")
print(getDuplicateRemovalUsingNestedLoop([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(getDuplicateRemovalUsingNestedLoop([5, 5, 5, 5, 5]))  # [5]
print(getDuplicateRemovalUsingNestedLoop([]))  # []
print(getDuplicateRemovalUsingNestedLoop([3, 1, 2, 2, 1]))  # [3, 1, 2] (original order)
