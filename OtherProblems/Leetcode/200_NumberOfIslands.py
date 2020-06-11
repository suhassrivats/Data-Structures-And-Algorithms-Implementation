class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time Complexity: O(mn)
        Space Complexity:
            Input Space: O(mn)
            Auxiliary Space: O(depth) => O(mn * memory for each call) => O(mn)
                - O(mn * memory for each call): For call-stack, in the worst
                case, it could be all 1s. Each recursive call might take some
                more space.
            Total Space => Input + Auxiliary
                        => O(mn) + O(mn * memory for each call)
                        => O(mn * memory for each call)
                        => O(mn)
        """
        # If input is empty, then there can be no islands. Return 0
        if not grid:
            return 0

        # Counter to keep track of the number of islands
        count = 0

        # Find the length of rows and cols
        rows = len(grid)
        cols = len(grid[0])

        # For every element in the matrix, check all its adjacent elements
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        # Boundary case for matrix
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return

        # Mark the cell as visited
        grid[i][j] = '#'

        # Make recursive calls in all four adjacent directions
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
