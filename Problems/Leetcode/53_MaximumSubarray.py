class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = nums[0]
        global_current = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            if max_current > global_current:
                global_current = max_current

        return global_current
