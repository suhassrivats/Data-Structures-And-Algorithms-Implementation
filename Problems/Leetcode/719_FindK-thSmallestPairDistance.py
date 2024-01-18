class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def countValidPairs(d):
            l, r = 0, 1
            count = 0
            while r < len(nums):
                if nums[r] - nums[l] <= d:
                    count += r - l
                    r += 1
                else:
                    l += 1
            return count

        # Min possible distance
        left = min([nums[i+1] - nums[i] for i in range(len(nums)-1)])
        # Max possible distance
        right = nums[len(nums)-1] - nums[0]

        # Binary search to see if some distance can atleast have k pairs
        while left < right:
            mid = (left + right) // 2
            if countValidPairs(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left