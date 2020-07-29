class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time complexity: O(n). Single loop up to n.
        Space complexity (auxiliary): O(n). dp array of size n is used.
        """
        if n <= 1:
            return 1

        # To store 0 stairs.
        ways = [None] * (n+1)
        ways[0] = 1  # Number of ways to get to 0 stairs is 1
        ways[1] = 1

        for i in range(2, n+1):
            ways[i] = ways[i-2] + ways[i-1]

        return ways[n]
