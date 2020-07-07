class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums)-1

        # If the array is in ascending order, return the first element
        if nums[right] > nums[left]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                if nums[mid] != nums[right]:
                    right = mid
                else:
                    right -= 1

        return nums[left]
