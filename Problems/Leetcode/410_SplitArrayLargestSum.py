class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        If k=1, sum = total of all elements (highest)
        if k=len(nums), sum=max(nums)

        Since sum is always in the above range, we can use binary search
        """

        def canSplit(largest):
            curr_sum = 0
            subarray = 0
            for num in nums:
                curr_sum += num
                if curr_sum > largest:
                    subarray += 1
                    # We want the next counting to start from current number
                    curr_sum = num
            # We need to add 1 as we are incrementing subarray only at the beginning of next subarray. This means last one will be left out if we don't add it
            return subarray+1 <= k

        l, r = max(nums), sum(nums)
        result = r
        while l <= r:
            mid = (l + r) // 2

            # We are able to split the subarrays equal to 2, then try to reduce largest value
            if canSplit(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result
