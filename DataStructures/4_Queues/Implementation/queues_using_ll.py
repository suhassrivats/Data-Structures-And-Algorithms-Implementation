# Queue implementation using Linked List


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, item):
        """A method to an item to the queue"""
        new_node = Node(item)

        if self.front == self.rear == None:
            self.front = self.rear = new_node
            return
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """A method to delete an item from the queue"""
        if self.is_empty():
            return
        else:
            temp = self.front
            self.front = temp.next

            if self.front is None:
                self.rear == None

        return str(temp.data)

    def display(self):
        """Display all the items in a Queue"""
        temp = self.front
        while temp:
            print(temp.data, "<-", end=" ")
            temp = temp.next
        print('\n')


# Driver code
if __name__ == '__main__':
    q = Queue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(90)
    q.display()
    q.dequeue()
    q.display()
