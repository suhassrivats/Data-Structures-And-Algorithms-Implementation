class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Time complexity:
            The time complexity of the above algorithm is O(n).

        Space complexity:
            The algorithm runs in constant space O(1).
        """

        i, n = 0, len(nums)

        while i < n:
            j = nums[i] - 1
            # If value and index are not equal, swap.
            # Ignore all negative numbers and numbers greater than n
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return n+1
