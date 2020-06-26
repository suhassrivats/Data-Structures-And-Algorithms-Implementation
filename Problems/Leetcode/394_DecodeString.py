class Solution:
    def decodeString(self, s: str) -> str:
        """
        Time Complexity: O(n) // n is the length of string
        Space Complexity: O(n) // curr_string + curr_num = n
        """
        curr_string = ''
        curr_num = 0
        stack = []

        for c in s:
            if c == '[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ''
                curr_num = 0
            elif c == ']':
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + (num * curr_string)
            elif c.isdigit():
                curr_num = curr_num * 10 + int(c)
            else:
                curr_string += c

        return curr_string
