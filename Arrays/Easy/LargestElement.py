def fourth_largest(arr):
    if len(arr) < 4 or len(arr) == 0:
        return None

    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    fourth = float('-inf')

    for num in arr:
        if num > first:
            fourth = third
            third = second
            second = first
            first = num
        elif num > second and num != first:
            fourth = third
            third = second
            second = num
        elif num > third and num != first and num != second:
            fourth = third
            third = num
        elif num > fourth and num != first and num != second and num != third:
            fourth = num

    if fourth == float('-inf'):
        return None

    return fourth

def main():
    test_arrays = [
        [],  # Edge case: empty array
        [5],  # Edge case: single element array
        [5, 5],  # Case: both elements are the same
        [1, 2, 3, 4, 5],  # Normal case: distinct elements
        [10, 5, 2, 10, 5],  # Case: some duplicate elements
        [2, 2, 2, 2, 2]  # Case: all elements are the same
    ]

    for arr in test_arrays:
        result = fourth_largest(arr)
        print(f"Array: {arr} => Fourth Largest: {result if result is not None else 'None'}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
