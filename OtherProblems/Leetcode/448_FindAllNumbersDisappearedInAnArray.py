class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # Subtract 1 from number to get an index
            index = abs(nums[i])-1

            # Mark number in the index as a negative value
            nums[index] = -abs(nums[index])

        # The missing numbers are position of the positive number + 1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
