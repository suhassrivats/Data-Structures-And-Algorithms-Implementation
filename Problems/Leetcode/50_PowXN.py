class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Time complexity: O(logn)
        Space complexity (auxiliary): O(logn)
        """

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            y = self.myPow(x, n/2)
            return y*y
        return x * self.myPow(x, n-1)
