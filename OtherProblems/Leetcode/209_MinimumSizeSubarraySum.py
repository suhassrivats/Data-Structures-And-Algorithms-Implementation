class Solution:
    # Time complexity: O(n^2)
    # Space complexity (Auxiliary): O(1)
    # Status: Time limit exceeded

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = len(nums) + 100
        total = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= s:
                    min_length = min(min_length, (j-i)+1)
                    break

        if min_length == len(nums) + 100:
            return 0
        else:
            return min_length


class Solution:
    """
    Time complexity: O(n)
        - While loop will only run once not for every iteration of for loop
    Space complexity (auxiliary): O(1)
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = len(nums) + 100
        total = 0
        left = 0

        for right, num in enumerate(nums):
            total += num

            while total >= s:
                min_length = min(min_length, right-left+1)
                total -= nums[left]
                left += 1

        if min_length <= len(nums):
            return min_length
        else:
            return 0
