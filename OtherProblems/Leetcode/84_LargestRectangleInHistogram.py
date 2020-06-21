class Solution:
    def largestRectangleArea(self, heights):
        """
        Idea: For any particular tower, width can be expanded only if heights
        of corresponding towers are equal to or greater than the current tower.
        Therefore, we need to find the nearest_smaller_element_left and
        nearest_smaller_element_right towers so that we know we cannot expand
        beyond it. We then store its range (width) in a separate array. Area is
        height * width. The results for each tower is stored in an array, we can
        then return the maximum area return the expected result.

        Useful link:
        https://www.youtube.com/watch?v=J2X70jj_I1o&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=7

        Complexity analysis:
        - Time Complexity: O(n)
        - Space Complexity (auxiliary): O(n)
        """
        if not heights or (len(heights) == 1 and heights[0] <= 0):
            return 0

        area = []
        widths = []

        if len(heights) == 1:
            widths.append(1)
        else:
            right = nearest_smaller_element_right(heights)
            left = nearest_smaller_element_left(heights)

            # Populate the widths array
            for i in range(len(heights)):
                widths.append(right[i] - left[i] - 1)

        # Populate the area array
        for i in range(len(heights)):
            area.append(heights[i] * widths[i])

        return max(area)


def nearest_smaller_element_right(arr):
    stack = []
    output = []
    psuedo_index = len(arr)

    # Append the smaller number to right's index
    for i in range(len(arr)-1, -1, -1):
        if not stack:
            output.append(psuedo_index)
        elif stack and stack[-1][0] < arr[i]:
            output.append(stack[-1][1])
        elif stack and stack[-1][0] >= arr[i]:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                output.append(psuedo_index)
            else:
                output.append(stack[-1][1])
        stack.append((arr[i], i))

    return output[::-1]


def nearest_smaller_element_left(arr):
    stack = []
    output = []
    psuedo_index = -1

    # Append the smaller number to left's index
    for i in range(len(arr)):
        if not stack:
            output.append(psuedo_index)
        elif stack and stack[-1][0] < arr[i]:
            output.append(stack[-1][1])
        elif stack and stack[-1][0] >= arr[i]:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if not stack:
                output.append(-1)
            else:
                output.append(stack[-1][1])
        stack.append((arr[i], i))

    return output
