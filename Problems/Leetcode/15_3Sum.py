class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity:
            Sorting the array will take O(N∗logN). The searchPair() function
        will take O(N). As we are calling searchPair() for every number in
        the input array, this means that overall threeSum() will take
        O(N*logN + N^2), which is asymptotically equivalent to O(N^2).

        Space complexity:
            Ignoring the space required for the output array, the space
        complexity of the above algorithm will be O(N) which is required for
        sorting.
        """
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip same element to avoid duplicate triplets
            self.search_pair(nums, -nums[i], i+1, triplets)

        return triplets

    def search_pair(self, nums, target_sum, left, triplets):
        right = len(nums)-1
        while left < right:
            current_sum = nums[left] + nums[right]
            if target_sum == current_sum:
                triplets.append([-target_sum, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif target_sum > current_sum:
                left += 1
            else:
                right -= 1
