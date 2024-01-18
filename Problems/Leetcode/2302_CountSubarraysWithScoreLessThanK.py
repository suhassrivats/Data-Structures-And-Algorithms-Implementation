class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total, res, j = 0, 0, 0
        for i, num in enumerate(nums):
            total += num
            # Check if total * window_len < k. If not, reduce window size
            while total * (i - j + 1) >= k:
                total -= nums[j]
                j += 1
            res += (i - j + 1)
        return res
