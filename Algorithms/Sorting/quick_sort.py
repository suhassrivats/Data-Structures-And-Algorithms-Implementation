class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums

        return self.quickSort(nums, 0, len(nums)-1)

    def partition(self, nums, start, end):
        pivot = nums[start]
        low = start + 1
        high = end

        while True:
            while low <= high and nums[high] >= pivot:
                high = high - 1

            while low <= high and nums[low] <= pivot:
                low = low + 1

            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
            else:
                break

        nums[start], nums[high] = nums[high], nums[start]

        return high

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        pi = self.partition(nums, start, end)
        self.quickSort(nums, start, pi-1)
        self.quickSort(nums, pi+1, end)

        return nums
