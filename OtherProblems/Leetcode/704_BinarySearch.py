class Solution:
    def search(self, nums, target):
        """
        Time Complexity: O(log N)
        Space Complexity (auxiliary): O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_element = nums[mid_index]

            if nums[mid_index] == target:
                return mid_index
            elif target < nums[mid_index]:
                right = mid_index - 1
            else:
                left = mid_index + 1

        return -1


class Solution:
    def search(self, nums, target):
        """
        Time Complexity: O(log N)
        Space Complexity (auxiliary): O(log N) // for call-stack
        """
        return self.search_helper(nums, target, 0, len(nums)-1)

    def search_helper(self, nums, target, left, right):
        if left > right:
            return -1
        mid_index = (left + right) // 2
        mid_element = nums[mid_index]

        if target == mid_element:
            return mid_index
        elif target < mid_element:
            return self.search_helper(nums, target, left, mid_index-1)
        else:
            return self.search_helper(nums, target, mid_index+1, right)
