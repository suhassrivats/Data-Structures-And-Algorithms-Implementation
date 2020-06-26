class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        curr_min = self.getMin()
        if (curr_min is None) or (x < curr_min):
            curr_min = x
        self.stack.append((x, curr_min))

    def pop(self) -> None:
        pop_item = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
