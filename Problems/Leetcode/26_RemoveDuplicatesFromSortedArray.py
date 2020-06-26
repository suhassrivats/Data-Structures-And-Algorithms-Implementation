class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[size] = nums[i]
                size += 1

        return size
