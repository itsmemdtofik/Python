def input_matrix(name: str) -> list[list[int]]:
    while True:
        try:
            rows = int(input(f"Enter rows for Matrix {name}: "))
            cols = int(input(f"Enter columns for Matrix {name}: "))
            matrix = []
            print(f"Enter elements for Matrix {name} (space-separated):")
            for i in range(rows):
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError("Invalid element count.")
                matrix.append(row)
            return matrix
        except ValueError as e:
            print(f"Error: {e}. Try again.")


def print_matrix(matrix: list[list[int]], title: str) -> None:
    """Print a matrix with a title."""
    print(f"\n{title}:")
    for row in matrix:
        print("  ".join(map(str, row)))


def add_matrices(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    result = []
    for i in range(len(nums1)):
        row = []
        for j in range(len(nums1[0])):
            row.append(nums1[i][j] + nums2[i][j])
        result.append(row)
    return result


def subtract_matrices(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    result = []
    for i in range(len(nums1)):
        row = []
        for j in range(len(nums1[0])):
            row.append(nums1[i][j] - nums2[i][j])
        result.append(row)
    return result


def multiply_matrices(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]] | None:
    if len(nums1[0]) != len(nums2):
        print("Cannot multiply: Columns of A must equal rows of B.")
        return None

    result = []
    for i in range(len(nums1)):
        row = []
        for j in range(len(nums2[0])):
            val = 0
            for k in range(len(nums2)):
                val += nums1[i][k] * nums2[k][j]
            row.append(val)
        result.append(row)
    return result


def transpose_matrix(nums: list[list[int]]):
    result = []
    for i in range(len(nums[0])):
        row = []
        for j in range(len(nums)):
            row.append(nums[j][i])
        result.append(row)
    return result


A = input_matrix("A")
B = input_matrix("B")

result_add = add_matrices(A, B)
print_matrix(result_add, "A + B")

result_sub = subtract_matrices(A, B)
print_matrix(result_sub, "A - B")

result_mul = multiply_matrices(A, B)
if result_mul:
    print_matrix(result_mul, "A x B")

result_transpose = transpose_matrix(A)
print_matrix(result_transpose, "Transpose of A")
