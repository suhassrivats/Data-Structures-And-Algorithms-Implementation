class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        # Return an empty list if matrix is empty
        if not matrix or not matrix[0]:
            return []

        # If matrix has contents in it
        result = []
        i = j = 0
        M = len(matrix)  # Row length
        N = len(matrix[0])  # Column length
        ans = []
        direction = 'UP'

        while (i, j) != (M-1, N-1):
            result.append(matrix[i][j])

            if direction == 'UP':
                if j == N-1:  # Right most col
                    i += 1
                    direction = 'DOWN'
                elif i == 0:  # Already at the very top row
                    j += 1
                    direction = 'DOWN'
                else:
                    i -= 1
                    j += 1

            else:
                if i == M-1:  # Last row
                    j += 1
                    direction = 'UP'
                elif j == 0:  # First column
                    i += 1
                    direction = 'UP'
                else:
                    i += 1
                    j -= 1

        result.append(matrix[M-1][N-1])

        return result
