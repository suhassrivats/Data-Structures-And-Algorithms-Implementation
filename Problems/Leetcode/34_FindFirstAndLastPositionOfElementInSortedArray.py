class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        # Find first and last occurence of the given target
        result[0] = self.findStartingIndex(nums, target)
        result[1] = self.findEndingIndex(nums, target)

        return result

    def findStartingIndex(self, nums, target):
        index = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_element = nums[mid_index]

            if mid_element >= target:
                right = mid_index - 1
            else:
                left = mid_index + 1

            if mid_element == target:
                index = mid_index

        return index

    def findEndingIndex(self, nums, target):
        index = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_element = nums[mid_index]

            if mid_element <= target:
                left = mid_index + 1
            else:
                right = mid_index - 1

            if mid_element == target:
                index = mid_index

        return index
