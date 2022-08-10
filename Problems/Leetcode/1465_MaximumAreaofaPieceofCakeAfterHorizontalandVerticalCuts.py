class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        Naive Approach
        T: O(M*N)
        S: O(1)
        """

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        # Append h and w so that we get to calcuate area of the last row and col
        horizontalCuts.append(h)
        verticalCuts.append(w)

        largest_area = float('-inf')
        prev_height = 0
        for hcut in horizontalCuts:
            prev_width = 0
            for vcut in verticalCuts:
                area = (hcut - prev_height) * (vcut - prev_width)
                largest_area = max(area, largest_area)
                prev_width = vcut
            prev_height = hcut

        return largest_area % 1000000007


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        Optimal Approach
        T: O(M+N)
        S: O(1)
        """
        
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        
        # Append h and w so that we get to calcuate area of the last row and col
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        # Find max_height
        max_height = float('-inf')
        prev_height = 0
        for hcut in horizontalCuts:
            max_height = max(hcut-prev_height, max_height)
            prev_height = hcut
            
        # Find max_width
        max_width = float('-inf')
        prev_width = 0
        for vcut in verticalCuts:
            max_width = max(vcut-prev_width, max_width)
            prev_width = vcut
            
        # Calculate the largest area
        largest_area = max_height * max_width
        
        return largest_area % 1000000007