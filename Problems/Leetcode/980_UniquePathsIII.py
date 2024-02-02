class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def backtracking(i, j, non_obs):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] < 0:
                return

            if (i, j) == end and non_obs == 0:
                self.paths += 1
                return

            # Mark visited cell as -2
            grid[i][j] = -2
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dir in directions:
                ni = i + dir[0]
                nj = j + dir[1]
                backtracking(ni, nj, non_obs-1)
            grid[i][j] = 0

        rows, cols = len(grid), len(grid[0])
        # We keep track of number of non obstacles from start to end.
        non_obs = 0
        start, end = None, None

        # When we are travesing, we will decrement non_obs by 1. When it is 0, it means that we have visited all non obs

        for i in range(rows):
            for j in range(cols):
                # Starting position
                if grid[i][j] == 1:
                    start = (i, j)
                # Non obs including start and end positions
                if grid[i][j] != -1:
                    non_obs += 1
                if grid[i][j] == 2:
                    end = (i, j)

        self.paths = 0
        # We are passing non_obs-1 because we are passing the start position already
        backtracking(start[0], start[1], non_obs-1)
        return self.paths
