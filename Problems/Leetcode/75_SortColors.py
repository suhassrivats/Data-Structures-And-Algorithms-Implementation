class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time complexity:
            The time complexity of the above algorithm will be O(N) as we are
        iterating the input array only once.

        Space complexity:
            The algorithm runs in constant space O(1).
        """

        i = 0
        low, high = 0, len(nums)-1

        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
