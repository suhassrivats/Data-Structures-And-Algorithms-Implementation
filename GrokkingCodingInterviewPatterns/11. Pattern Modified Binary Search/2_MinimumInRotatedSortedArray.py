class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            # The minimum occurs where order breaks
            if nums[mid] > nums[mid + 1]:
                # nums[mid+1] is the minimum
                return nums[mid + 1]
            elif nums[mid] < nums[r]:
                # right half is sorted, go left
                r = mid
            else:
                # minimum is in right half
                l = mid + 1

        return nums[l]
