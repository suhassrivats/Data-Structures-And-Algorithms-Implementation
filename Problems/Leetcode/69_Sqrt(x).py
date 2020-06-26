class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity (auxiliary): O(1)
        """
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1
