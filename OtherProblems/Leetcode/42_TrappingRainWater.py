class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time Complexity: O(n) // n is length of the given array
        Space Complexity (auxiliary): O(n + n + n) => O(n)
            For max_left/right_height and water arrays

        Useful link: https://www.youtube.com/watch?v=FbGG2qpNp4U&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=9
        """

        if not height:
            return 0

        n = len(height)
        # Left and right arrays will contain max left/right values for a
        # specific height element in the array respectively
        max_left_height = [None] * len(height)
        max_right_height = [None] * len(height)
        water = [None] * len(height)

        max_left_height[0] = height[0]
        max_right_height[n-1] = height[n-1]

        for i in range(1, n):
            max_left_height[i] = max(max_left_height[i-1], height[i])

        for i in range(n-2, -1, -1):
            max_right_height[i] = max(max_right_height[i+1], height[i])

        for i in range(n):
            water[i] = min(max_left_height[i], max_right_height[i]) - height[i]

        return sum(water)
