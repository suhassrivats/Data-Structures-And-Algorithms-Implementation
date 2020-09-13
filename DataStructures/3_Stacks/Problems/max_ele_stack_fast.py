# Find maximum element in a stack using array (Fast solution)

"""
You have an empty sequence, and you will be given  queries.
Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
"""

class CustomStack:

    def __init__(self):
        self.stack = []
        self.maxima = []

    def push(self, data):
        self.stack.append(data)

        # Append only greater number to the list
        if not self.maxima or data >= self.maxima[-1]:
            self.maxima.append(data)

    def pop(self):
        popitem = self.stack.pop()
        if popitem == self.maxima[-1]:
            self.maxima.pop()

    def max_data(self):
        print(self.maxima[-1])

def main():

    stack = CustomStack()
    N = int(input())

    for i in range(N):
        # Get the input along with instruction
        inp = input()
        if len(inp.split()) == 2:
            command, data = map(int, inp.split())
        else:
            command = int(inp[0])

        if command == 1:
            stack.push(data)
        elif command == 2:
            stack.pop()
        else:
            stack.max_data()




if __name__ == "__main__":
    main()

