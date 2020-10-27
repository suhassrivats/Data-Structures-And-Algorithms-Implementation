# Brute force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j-i))
        return max_area


# Two Pointer Approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        water = 0
        while i < j:
            water = max(water, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
