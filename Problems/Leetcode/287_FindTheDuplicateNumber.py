class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                j = nums[i]-1
                # index and value should be equal. Swap otherwise
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i]
            else:
                i += 1
        return -1


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)


# class Solution:
#     def findDuplicate(self, nums):
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return nums[i]
