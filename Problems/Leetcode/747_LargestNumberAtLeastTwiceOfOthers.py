class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0

        for i, n in enumerate(nums):

            # Find the highest number
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i

            # Find the second highest number
            elif n > secondHighest:
                secondHighest = n

        if highest < 2 * secondHighest:
            return -1

        return highestIndex
