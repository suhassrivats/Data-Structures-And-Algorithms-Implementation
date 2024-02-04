class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        n, m = len(matrix), len(matrix[0])
        longest_path = 0
        cache = [ [0 for _ in range(m)] for _ in range(n) ]

        def recurse(matrix, cache, n, m, i, j):
            if cache[i][j] > 0:
                return cache[i][j]
            maxlen = 0
            for d in directions:
                ni = i + d[0]
                nj = j + d[1]
                if ni > -1 and nj > -1 and ni < n and nj < m and matrix[ni][nj] > matrix[i][j]:
                    longest = recurse(matrix, cache, n, m, ni, nj)
                    maxlen = max(maxlen, longest)
            cache[i][j] = maxlen + 1
            return cache[i][j]

        for i in range(n):
            for j in range(m):
                longest = recurse(matrix, cache, n, m, i, j)
                longest_path = max(longest_path, longest)
        return longest_path
