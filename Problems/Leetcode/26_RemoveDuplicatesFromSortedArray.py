class Solution:
    """
    Complexity analysis:
        Time complextiy : O(n). Assume that n is the length of array. Here i
            traverses once per array
        Space complexity : O(1)
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        size = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[size] = nums[i]
                size += 1

        return size
