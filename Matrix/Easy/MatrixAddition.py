# Matrix Operations without NumPy

def input_matrix(name):
    print(f"\nEnter the size of Matrix {name} (rows and columns):")
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

    print(f"Enter the elements of Matrix {name} row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print("Column count mismatch. Try again.")
            return input_matrix(name)
        matrix.append(row)
    return matrix


def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print("  ".join(map(str, row)))


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible: columns of A ≠ rows of B.")
        return None
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(val)
        result.append(row)
    return result


def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


# Main program
if __name__ == "__main__":
    print("Matrix Operation Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")

    choice = input("Enter your choice (1-4): ")

    if choice in ['1', '2', '3']:
        A = input_matrix("A")
        B = input_matrix("B")

        if choice == '1':
            result = add_matrices(A, B)
            print_matrix(result, "A + B")

        elif choice == '2':
            result = subtract_matrices(A, B)
            print_matrix(result, "A - B")

        elif choice == '3':
            result = multiply_matrices(A, B)
            if result:
                print_matrix(result, "A x B")

    elif choice == '4':
        A = input_matrix("A")
        result = transpose_matrix(A)
        print_matrix(result, "Transpose of A")

    else:
        print("Invalid choice. Please select between 1 to 4.")
