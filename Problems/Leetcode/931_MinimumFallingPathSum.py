class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        T: O(M*N)
        C: In-place, O(M*N)
        """
        for row in range(1, len(matrix)):  # starting from 1st row
            for col in range(len(matrix[0])):
                if col == 0:  # left most col
                    matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col+1])
                elif col == len(matrix[0]) - 1:  # right most col
                    matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col-1])
                else:  # everything in between
                    matrix[row][col] += min(matrix[row-1][col-1], matrix[row-1]
                                            [col], matrix[row-1][col+1])
        return min(matrix[-1])
