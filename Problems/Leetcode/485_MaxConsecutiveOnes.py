class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity (auxiliary): O(1)
        """

        max_1s = 0
        temp = 0

        for num in nums:
            if num == 1:
                temp += 1
            elif num == 0:
                if max_1s < temp:
                    max_1s = temp
                temp = 0
        if max_1s < temp:
            max_1s = temp

        return max_1s
