# Find maximum element in a Stack using Linked List (Slow solution)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            print("Stack is empty")
            return False

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        popnode = self.head
        self.head = self.head.next
        popnode.next = None

    def max_element(self):
        elements = []
        temp = self.head
        while(temp):
            elements.append(temp.data)
            temp = temp.next
        print(max(elements))
        return max(elements)


def main():
    stack = Stack()
    N = int(input())

    for _ in range(N):
        unknown = input()

        command = unknown[0]

        if command == '1':
            cmd, value = map(int, unknown.split())
            stack.push(value)
        elif command == '2':
            stack.pop()
        else:
            stack.max_element()


if __name__ == "__main__":
    main()
