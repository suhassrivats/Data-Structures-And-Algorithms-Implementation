class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float('-inf')
        window_start, window_sum = 0, 0.0

        for window_end in range(len(nums)):
            window_sum += nums[window_end]

            if window_end >= k-1:
                window_avg = window_sum/k
                result = max(result, window_avg)
                window_sum -= nums[window_start]
                window_start += 1

        return result
