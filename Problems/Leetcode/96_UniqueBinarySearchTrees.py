import math


# Catalan Number  (2n)!/((n+1)!*n!)
class Solution:
    def numTrees(self, n: int) -> int:
        return math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))
