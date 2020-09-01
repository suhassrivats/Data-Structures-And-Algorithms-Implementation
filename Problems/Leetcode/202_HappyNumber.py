class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Time Complexity:
            The time complexity of the algorithm is difficult to determine.
            However we know the fact that all unhappy numbers eventually get
            stuck in cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

            This sequence behavior tells us two things:

            If the number NN is less than or equal to 1000, then we reach the
            cycle or ‘1’ in at most 1001 steps. For N > 1000N>1000, suppose the
            number has ‘M’ digits and the next number is ‘N1’. From the above
            Wikipedia link, we know that the sum of the squares of the digits
            of ‘N’ is at most 9^2*M, or 81M (this will happen when all digits
            of ‘N’ are ‘9’).
            This means:

            N1 < 81M
            As we know M = log(N+1)
            Therefore: N1 < 81 * log(N+1) => N1 = O(logN)
            This concludes that the above algorithm will have a time complexity
            of O(logN).

        Space Complexity: O(logN)
        """

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


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Time Complexity:
            Same as above O(logN)
        Space Complexity: O(1)
        """
        slow, fast = n, n
        while True:
            slow = self.find_square_sum(slow)  # move one step
            fast = self.find_square_sum(self.find_square_sum(fast))  # move two steps
            if slow == fast:  # found the cycle
                break
        return slow == 1  # see if the cycle is stuck on the number '1'

    def find_square_sum(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit*digit
            n //= 10
        return total
