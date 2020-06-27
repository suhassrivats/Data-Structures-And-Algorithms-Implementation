class Solution:
    def findMin(self, nums: List[int]) -> int:

        # If there are no elements in the array
        if not nums:
            return None

        # If there is only one element in the array, then return that element
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # If the last element is greater than the first element, then there is
        # no rotation. First element is the smallest element in this case
        if nums[right] > nums[0]:
            return nums[0]

        # Binary Search
        while right >= left:
            mid = (left + right) // 2

            # This would be the point of change from higher to lower value
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            # Point of change from higher to lower value
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this
            # means the least value is still somewhere to the right as we are
            # still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
