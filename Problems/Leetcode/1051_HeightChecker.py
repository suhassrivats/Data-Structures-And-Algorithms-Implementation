class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0

        for a, b in zip(heights, sorted(heights)):
            if a != b:
                count += 1

        return count
