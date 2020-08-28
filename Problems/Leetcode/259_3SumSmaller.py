class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Time complexity:
            Sorting the array will take O(N * logN). The searchPair() will
        take O(N). So, overall searchTriplets() will take O(N * logN + N^2),
        which is asymptotically equivalent to O(N^2)

        Space complexity:
            The space complexity of the above algorithm will be O(N) which is
        required for sorting if we are not using an in-place sorting algorithm.
        """

        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            count += self.searchPair(nums, target-nums[i], i)
        return count

    def searchPair(self, nums, target_sum, i):
        count = 0
        left, right = i+1, len(nums)-1
        while left < right:
            if nums[left] + nums[right] < target_sum:  # found the triplet
                # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
                # left and right to get a sum less than the target sum
                count += right - left
                left += 1
            else:
                right -= 1
        return count
