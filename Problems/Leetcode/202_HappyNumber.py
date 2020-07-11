class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:
            # Square each digits of n and find sum.
            n = sum([int(i)**2 for i in str(n)])

            # If n is already is in the set, there there is a loop.
            if n in seen:
                return False
            else:
                seen.add(n)

        return True
