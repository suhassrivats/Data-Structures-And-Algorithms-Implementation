class Solution:
    def calculate(self, s: str) -> int:
        """
        Time Complexity:
            O(N), where N is the length of the string
        Space Complexity:
            If 'P' is the sum of digits in parantheses and if there are k such
            parantheses, the space complexity is O(N - kP) => O(N)
        """

        num, sign, total = 0, 1, 0
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in '+-':
                total += num*sign
                if s[i] == '+':
                    sign = 1
                else:
                    sign = -1
                num = 0
            elif s[i] ==  '(':
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
            elif s[i] == ')':
                total += (num * sign)
                total = stack.pop() * total
                total += stack.pop()
                num = 0
        return total + num*sign
