class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Time Complexity:
            O(N) where N is the length of nums. left can only be incremented at
        most N times.

        Space Complexity:
            O(1) is the space used by prod, left, and ans.
        """

        if k <= 1:
            return 0
        prod = 1
        left = results = 0

        for right, val in enumerate(nums):
            prod *= val

            while prod >= k:
                prod /= nums[left]
                left += 1

            results += right - left + 1

        return results
