class Solution:
    def calculate(self, s: str) -> int:
        """
        Time Complexity #
            The time complexity of the above algorithm will be O(N) where ‘N’
            is the number of characters in the input string.

        Space Complexity #
            O(1): Since we are only using variables such as res which occupies
                constant space.
        """
        i = 0
        cur = prev = res = 0
        cur_operation = '+'

        while i < len(s):
            cur_char = s[i]

            # if cur_char is a digit
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1

                if cur_operation == '+':
                    res += cur
                    prev = cur
                elif cur_operation == '-':
                    res -= cur
                    prev = -cur
                elif cur_operation == '*':
                    res -= prev
                    res += prev * cur
                    prev = cur * prev
                else:
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev/cur)

                cur = 0
            # If any operator
            elif cur_char != ' ':
                cur_operation = cur_char
            i += 1
        return res
