def spiralOrder(matrix):
    r = c = 0  # Starting at (r,c) = (0,0)
    m = len(matrix)
    n = len(matrix[0])
    last_row = m - 1
    last_col = n - 1
    results = []

    while (r <= last_row and c <= last_col):

        # Print first row
        for i in range(c, last_col+1):
            results.append(matrix[r][i])
        r += 1

        # Print first column
        for i in range(r, last_row+1):
            results.append(matrix[i][last_col])
        last_col -= 1

        if (r <= last_row):
            for i in range(last_col, c-1, -1):
                results.append(matrix[last_row][i])
            last_row -= 1

        if (c <= last_col):
            for i in range(last_row, r-1, -1):
                results.append(matrix[i][c])
            c += 1

    return results


# Tests
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(spiralOrder(matrix))
