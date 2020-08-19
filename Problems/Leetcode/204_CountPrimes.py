class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False

        # Iterate only till sqrt(n). Ex 5*5 is 25. We will be marking 25 as
        # False in our inner loop
        for i in range(2, int(n ** 0.5)+1):
            if primes[i]:
                # Mark multiples of all i as False. 2*1, 2*2, 2*3 ...
                for j in range(i*i, n, i):
                    primes[j] = False

        return sum(primes)
