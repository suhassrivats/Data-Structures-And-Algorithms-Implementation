class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Filter only unique elements in the list
        nums = set(nums)

        if len(nums) < 3:
            return max(nums)

        # Remove first two maximum elements from the set
        nums.remove(max(nums))
        nums.remove(max(nums))

        # Return the max element out of the remaning elements.
        # Note that first two max elements are removed already.
        return max(nums)
