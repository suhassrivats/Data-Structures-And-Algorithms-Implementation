class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity:
            Sorting the array will take O(N∗logN). Overall searchQuadruplets()
        will take O(N * logN + N^3), which is asymptotically equivalent to O(N^3)

        Space complexity:
            The space complexity of the above algorithm will be O(N) which is
        required for sorting.
        """

        quadraplets = []
        nums.sort()
        for i in range(0, len(nums)-3):
            # skip same element to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                # skip same element to avoid duplicate quadruplets
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                self.search_pairs(nums, target, i, j, quadraplets)
        return quadraplets

    def search_pairs(self, nums, target_sum, first, second, quadraplets):
        left = second + 1
        right = len(nums) - 1

        while (left < right):
            total = nums[first] + nums[second] + nums[left] + nums[right]

            if total == target_sum:  # found the quadraplet
                quadraplets.append([nums[first], nums[second],
                                    nums[left], nums[right]])
                left += 1  # skip same element to avoid duplicate quadruplets
                right -= 1  # skip same element to avoid duplicate quadruplets

                while left < right and nums[left] == nums[left-1]:
                    left += 1  # we need a pair with bigger sum
                while left < right and nums[right] == nums[right+1]:
                    right -= 1  # we need a pair with smaller sum

            elif total < target_sum:
                left += 1
            else:
                right -= 1
