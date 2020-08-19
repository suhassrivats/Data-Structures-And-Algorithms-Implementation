class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_frequency_map = {}

        for num in nums:
            num_frequency_map[num] = num_frequency_map.get(num, 0) + 1

        for k, v in num_frequency_map.items():
            if v > len(nums)//2:
                return k
