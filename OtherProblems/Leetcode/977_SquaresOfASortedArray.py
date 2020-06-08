class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity (auxiliary): O(1)
        """

        even_dig_counter = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_dig_counter += 1
        return even_dig_counter
