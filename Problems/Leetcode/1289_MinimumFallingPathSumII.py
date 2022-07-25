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

            for j in range(cols):
                # If the smallest element in the previous row in the same col
                if prev_row[j] == prev_min1_value:
                    arr[i][j] += prev_min2_value
                else:
                    arr[i][j] += prev_min1_value

        return min(arr[-1])  # take min of last row
