class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Time complexity:
            The time complexity of the above algorithm will be O(N).

        Space complexity:
            The algorithm runs in constant space O(1).
        """

        low, high = 0, len(nums)-1

        # find the first number out of sorting order from the beginning
        while (low < len(nums)-1) and (nums[low] <= nums[low+1]):
            low += 1

        # if the array is sorted
        if low == len(nums)-1:
            return 0

        # find the first number out of sorting order from the end
        while (high > 0 and (nums[high] >= nums[high-1])):
            high -= 1

        # find the minimum and maximum of the subarray
        subarray_max = float('-inf')
        subarray_min = float('inf')
        for k in range(low, high+1):
            subarray_max = max(subarray_max, nums[k])
            subarray_min = min(subarray_min, nums[k])

        # extend the subarray to include any number which is bigger than the minimum of the subarray
        while low > 0 and nums[low-1] > subarray_min:
            low -= 1

        # extend the subarray to include any number which is smallar than the maximum of the subarray
        while high < len(nums)-1 and nums[high+1] < subarray_max:
            high += 1

        return high - low + 1
