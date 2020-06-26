def generate_pascal_triangle(numRows):

    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]

    triangle = [[1]]

    for i in range(1, numRows):
        # The first and last row elements are always 1.
        row = [1]  # first

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, i):
            row.append(triangle[i-1][j-1]+triangle[i-1][j])
        row.append(1)  # last

        # Apprend the new row (list) to triangle (list of lists)
        triangle.append(row)

    return triangle


# Tests
print(generate_pascal_triangle(5))
