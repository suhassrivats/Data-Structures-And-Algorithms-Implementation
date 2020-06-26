class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Check if nums is empty or if there is only one element
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        left = 0
        right = len(nums) - 1
        result = 0

        # If the array is fully sorted, then perform a simple binary search.
        # Othewise, find pivot_index.
        if nums[left] < nums[right]:
            result = self.binary_search(left, right, nums, target)
        else:
            pivot_index = self.find_pivot(left, right, nums)

            # Check in which sorted array does target may lie
            if target >= nums[pivot_index] and target <= nums[right]:
                result = self.binary_search(pivot_index, right, nums, target)
            else:
                result = self.binary_search(left, pivot_index-1, nums, target)

        return result

    def binary_search(self, left, right, nums, target):

        while left <= right:
            mid_index = (left + right) // 2
            mid_element = nums[mid_index]

            if target == mid_element:
                return mid_index
            elif target < mid_element:
                right = mid_index - 1
            else:
                left = mid_index + 1

        return -1

    def find_pivot(self, left, right, nums):
        mid_index = (left + right) // 2
        pivot_index = 0

        # If array were sorted, then mid+1 would be greater than mid. If not,
        # we have found our pivot_index
        if nums[mid_index] > nums[mid_index+1]:
            return mid_index+1
        else:
            # Check in which side pivot_index may lie
            if nums[left] > nums[mid_index]:
                # It means that pivot is in right of mid_index
                pivot_index = self.find_pivot(left, mid_index-1, nums)
            else:
                # Check in the left sorted array
                pivot_index = self.find_pivot(mid_index+1, right, nums)

        return pivot_index
