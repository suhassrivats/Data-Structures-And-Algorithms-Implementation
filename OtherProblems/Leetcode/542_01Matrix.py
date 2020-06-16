import collections


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(r⋅c)
            Since, the new cells are added to the queue only if their current
            distance is greater than the calculated distance, cells are not
            likely to be added multiple times.

        Space complexity: O(r⋅c) // Additional O(r⋅c) for queue
        """
        # Find the length of rows and cols
        rows = len(matrix)
        cols = len(matrix[0])
        queue = collections.deque()
        output = [[val*200 for val in r] for r in matrix]

        # Get cooridinates when matrix value is zero and store it queue
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for mi, mj in self.dfs(i, j, rows, cols, output):
                queue.append((mi, mj))
                output[mi][mj] = output[i][j] + 1

        return output

    def dfs(self, i, j, rows, cols, output):
        # Movement for top, bottom, left and right
        for mi, mj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if 0 <= mi < rows and 0 <= mj < cols and output[mi][mj] == 200:
                yield mi, mj
