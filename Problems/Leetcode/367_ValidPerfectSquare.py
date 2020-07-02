class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Time Complexity: O(log(sqrt(n))) // If n were 25, we are running the
        loop only 5 times. We are then applying binary search on this.
        Space Complexity (auxiliary): O(1) // no extra space needed
        """

        left = 0
        right = num

        while left <= right:
            mid = left + (right-left)//2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
