class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        T: O(n)
        S: O(n)
        """
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result
