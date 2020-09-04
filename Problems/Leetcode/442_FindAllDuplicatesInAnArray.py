class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Time complexity:
            The time complexity of the above algorithm is O(n).

        Space complexity:
            Ignoring the space required for storing the duplicates, the
        algorithm runs in constant space O(1).
        """

        i = 0
        duplicate_numbers = []

        while i < len(nums):
            j = nums[i]-1
            # if the value is not equal to its index, swap
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                duplicate_numbers.append(nums[i])

        return duplicate_numbers
