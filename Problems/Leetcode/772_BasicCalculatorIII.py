class Solution:
    """
    @param s: the expression string
    @return: the answer
    """

    def calculate(self, s: str) -> int:
        # Write your code here
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        num = 0
        op = '+'
        stack = []

        def helper(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                stack.append(int(stack.pop() / num))

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                stack.append(op)
                num = 0
                op = '+'
            elif s[i] in ['+', '-', '/', '*', ')']:
                helper(op, num)
                if s[i] == ')':
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    helper(op, num)
                num = 0
                op = s[i]
        helper(op, num)

        return sum(stack)
