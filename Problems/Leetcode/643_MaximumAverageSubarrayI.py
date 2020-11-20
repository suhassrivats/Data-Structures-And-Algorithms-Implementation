# Brute Force
class Solution:
    """
    Time complexity: O(n * k)
    Space complexity (auxiliary): O(1)
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = []
        for i in range(len(nums)-k+1):
            total = 0
            for j in range(i, i+k):
                total += nums[j]
            result.append(total/k)
        return max(result)


# Optimized - Sliding window
class Solution:
    """
    Time complexity: O(n)
    Space complexity (auxiliary): O(1)
    """

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
