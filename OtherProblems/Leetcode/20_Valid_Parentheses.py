class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity : O(n) because we simply traverse the given string one
            character at a time and push and pop operations on a stack take O(1)
            time.
        Space Complexity : O(n) as we push all opening brackets onto the stack
            and in the worst case, we will end up pushing all the brackets onto
            the stack. e.g. ((((((((((.
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # Open brackets
            if char in bracket_map.values():
                stack.append(char)
            # Closed brackets
            elif char in bracket_map.keys():
                # Value of bracket_map[char] is an open bracket. Compare it
                # with popped open_bracket from the stack
                if not stack or bracket_map[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []
