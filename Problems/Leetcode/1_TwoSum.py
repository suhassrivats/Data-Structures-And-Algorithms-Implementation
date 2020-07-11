class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        tracker = {}
        for index, key in enumerate(nums):
            tracker[key] = index

        for index, key in enumerate(nums):
            complement = target - nums[index]

            # Make sure that the other number which sums up to target is in
            # dictionary. Also, if there are two same numbers (such as 2+2=4)
            # provide the index of the other number
            if (complement in tracker) and (tracker[complement] != index):
                return [index, tracker[complement]]

        return None
