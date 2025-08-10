# Finding a peak element in 2D array
def findPeakGrid(arr):
    result = []
    row = len(arr)
    column = len(arr[0])

    for i in range(row):
        for j in range(column):

            # checking with top element
            if i > 0:
                if arr[i][j] < arr[i - 1][j]:
                    continue
            # checking with right element
            if j < column - 1:
                if arr[i][j] < arr[i][j + 1]:
                    continue
            # checking with bottom element
            if i < row - 1:
                if arr[i][j] < arr[i + 1][j]:
                    continue
            # checking with left element
            if j > 0:
                if arr[i][j] < arr[i][j - 1]:
                    continue

            result.append(i)
            result.append(j)
            break

    return result


# driver code
arr = [[9, 8], [2, 6]]
result = findPeakGrid(arr)
print("Peak element found at index:", result)

