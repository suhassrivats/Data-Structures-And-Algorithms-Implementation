# Implement a stack using singly linked list


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):

        if self.isempty():
            return None
        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            return popnode.data

    def peek(self):

        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):

        if self.isempty():
            print("Linked List is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data, "->", end=" ")
                temp = temp.next
            return


##########
# Driver code
MyStack = Stack()

MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

# Display stack elements
MyStack.display()

# Print top elementof stack
print("\nTop element is ", MyStack.peek())

# Delete top elements of stack
MyStack.pop()
MyStack.pop()

# Display stack elements
MyStack.display()

# Print top elementof stack
print("\nTop element is ", MyStack.peek())
