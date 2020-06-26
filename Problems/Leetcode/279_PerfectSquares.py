class Solution:
    def numSquares(self, n: int) -> int:
        """
        Time Complexity:
        We will check number from 1 to n so it takes O(n) iterations. In each
        iteration, we will check each candidate composition and find minimum of
        them, which takes O(k) time if k is counts of integers that square value
        is less than i in this iteration. Because k will be in range 1 and
        i^(1/2), it takes O(i^(1/2)) time in each iteration. Therefore, totally
        it will take O(1^(1/2)+2^(1/2)+… +n^(1/2)) = O(n(1+n^0.5)/2)
        = O(n/2 + (n^1.5)/2) = O(n^1.5) time for this approach

        Space Complexity:
        We use a distance list for saving all previous information so it will
        take O(n) space.
        """
        # Create a dp array with min number of squares for each of its index
        # value. For example, if the index is 5, its value initially is 5.
        # Which is formed by 1^2 + 1^2 + 1^2 + 1^2 + 1^2.
        dp = [_ for _ in range(n+1)]

        # Find minimum_squares and update the initial value
        for i in range(2, n+1):
            minimum_squares = i
            for j in range(1, i):
                # Check if any of the squares starting from 1 to i can be used
                # to find minimum_squares. If the minimum_squares is better than
                # the existing one, then update it in dp array. Ex, initially 4
                # has minimum_squares as 4 but 2^2 is also 4. We can now update
                # minimum_squares as 1
                next = j * j
                remaining = i-next

                # Make sure that remaining is always positive. For example, to
                # find minimum_squares of 4 we check square values of 1,2,3.
                # But remaining value when j=3 is 4-(3^2)=-5 which is not valid.
                if remaining < 0:
                    break
                else:
                    minimum_squares = min(minimum_squares, dp[remaining]+1)

            # Update the minimum_squares in dp array. minimum_squares value for
            # 4 will be updated to 1 (2^2) from 4 (1^2 + 1^2 + 1^2 + 1^2)
            if dp[i] == i:
                dp[i] = minimum_squares

        return dp[n]
