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


class Solution:
    def calculate(self, s: str) -> int:
        """
        Time Complexity #
            The time complexity of the above algorithm will be O(N) where ‘N’
            is the number of characters in the input string.

        Space Complexity #
            O(D): If D is the total number of digits in the string, then space
            complexity will be O(D). As stack should store all digits.
        """

        if not s:
            return "0"
        num, stack, sign = 0, [], '+'
        operators = ['+', '-', '*', '/']
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])  # Could be a number with more than 1 digit
            if s[i] in operators or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)
