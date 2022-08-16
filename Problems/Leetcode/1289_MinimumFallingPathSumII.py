import heapq


class Solution:
    def minFallingPathSum(self, arr) -> int:
        rows, cols = len(arr), len(arr[0])

        # If it is a grid with only one element, simply return the vaule [[1]]
        if rows == 1 and cols == 1:
            return arr[0][0]

        for i in range(1, rows):
            # Find minimum two values from the previous_row
            prev_row = arr[i-1]
            # min1
            prev_min1_value = min(prev_row)
            prev_min1_index = prev_row.index(prev_min1_value)
            # min2
            prev_min2_value = min(val for j, val in enumerate(prev_row) if j != prev_min1_index)
            prev_min2_index = prev_row.index(prev_min2_value)

            # Optimal way to find 2 minimum elements is to use heap
            # r = heapq.nsmallest(2, A[i - 1])

            for j in range(cols):
                # If the smallest element in the previous row is in the same col
                if prev_row[j] == prev_min1_value:
                    arr[i][j] += prev_min2_value
                else:
                    arr[i][j] += prev_min1_value

        return min(arr[-1])  # take min of last row


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """ 
        Optimal Approach

        Idea:
            - Start iteration from 1st row
            - Add min from prev row to the min of current row if they are not in same col
            - If they are in same col, add second min to the min of current row

        Walkthrough: arr = [[1,2,3],[4,5,6],[7,8,9]]

        1       2       3
        4+2     5+1     6+1
        7+6     8+6     9+6  
        """

        for row in range(1, len(grid)):
            prev_row = grid[row-1]
            # Find 2 minimum elements
            mins = heapq.nsmallest(2, prev_row)

            for col in range(len(grid[0])):
                # If the min element is the same column, then add second min element.
                if prev_row[col] == mins[0]:
                    grid[row][col] += mins[1]
                else:  # Else add min element
                    grid[row][col] += mins[0]
        return min(grid[-1])
