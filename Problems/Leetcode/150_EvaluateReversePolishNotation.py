class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time Complexity: O(n) //n is the length of the RPN expression. We will
        process all n operators/operands in the expression. Each will either
        entail an O(1) push/pop or an O(1) arithmetic calculation.

        Space Complexity (auxiliary): O(d)
            Let d be the total operands (numbers).
            Let b be the number of operators (+,  -,  *,  /)
            If we have d digits and b operators where d + b = n, we certainly
            will not use O(d + b) space (operators are not pushed to the stack).
        """
        valid_operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in valid_operators:
                stack.append(int(token))
            else:
                if stack:
                    # Pop the two items from the stack
                    second_item = stack.pop()
                    first_item = stack.pop()

                    if token == '+':
                        stack.append(first_item+second_item)
                    elif token == '-':
                        stack.append(first_item-second_item)
                    elif token == '*':
                        stack.append(first_item*second_item)
                    else:
                        stack.append(int(first_item/second_item))

        return stack.pop()
