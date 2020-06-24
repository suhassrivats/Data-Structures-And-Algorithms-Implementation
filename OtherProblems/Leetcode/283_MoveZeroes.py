class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_index = 0
        index = 0

        while index < len(nums) - 1:
            if nums[index] == 0:
                if nums[index+1] != 0:
                    nums[zero_index] = nums[index+1]
                    nums[index+1] = 0
                    zero_index += 1
                    index += 1
                else:
                    index += 1
            else:
                zero_index += 1
                index += 1
        return nums
