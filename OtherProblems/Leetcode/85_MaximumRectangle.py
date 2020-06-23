class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        prev_row = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            curr_row = [int(i) for i in row]
            for j in range(len(curr_row)):
                if curr_row[j] != 0:
                    curr_row[j] = curr_row[j] + prev_row[j]
                else:
                    curr_row[j] = 0
            max_area = max(max_area, self.largestRectangleArea(curr_row))
            prev_row = curr_row

        return max_area

    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        area = []
        widths = []

        right = self.next_smaller_element_right(heights)
        left = self.next_smaller_element_left(heights)

        # Populate the widths array
        for i in range(len(heights)):
            widths.append(right[i] - left[i] - 1)

        # Populate the area array
        for i in range(len(heights)):
            area.append(heights[i] * widths[i])

        return max(area)

    def next_smaller_element_right(self, arr):
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

    def next_smaller_element_left(self, arr):
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
