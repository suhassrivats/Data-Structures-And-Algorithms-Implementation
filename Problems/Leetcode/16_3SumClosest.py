class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Time complexity:
            Sorting the array will take O(N* logN). Overall threeSumClosest()
        will take O(N * logN + N^2), which is asymptotically equivalent to O(N^​2).

        Space complexity:
            The space complexity of the above algorithm will be O(N) which is
        required for sorting.
        """

        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):
            left, right = i+1, len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target-total) < abs(diff):
                    diff = target-total
                if total < target:
                    left += 1
                else:
                    right -= 1

            if diff == 0:
                break

        return target - diff
