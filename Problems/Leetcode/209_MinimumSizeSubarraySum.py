# Brute Force
class Solution:
    """
    Time complexity: O(n^2)
    Space complexity (Auxiliary): O(1)
    Status: Time limit exceeded
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = len(nums) + 100
        total = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= s:
                    min_length = min(min_length, (j-i)+1)
                    break
            total = 0

        if min_length == len(nums) + 100:
            return 0
        else:
            return min_length


# Sliding window
class Solution:
    """
    Time complexity: O(n)
        - While loop will only run once not for every iteration of for loop
    Space complexity (auxiliary): O(1)
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        window_start = 0
        window_sum = 0
        min_length = len(nums) + 1000

        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            while window_sum >= s:
                min_length = min(min_length, (window_end-window_start+1))
                window_sum -= nums[window_start]
                window_start += 1

        if min_length == len(nums) + 1000:
            return 0
        else:
            return min_length
