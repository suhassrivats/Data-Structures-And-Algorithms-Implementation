# Using recursion and memoization
class Solution:
    def fib(self, N: int) -> int:
        cache = {}

        def recur_fib(N):
            if N in cache:
                return cache[N]
            if N < 2:
                return N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)

            # Put result in cache for later reference
            cache[N] = result
            return result

        return recur_fib(N)
