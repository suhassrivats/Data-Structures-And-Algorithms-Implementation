# Implement Circular Queue using Linked List


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
            return
        else:
            temp = self.rear
            temp.next = new_node
            self.rear = temp.next
            self.rear.next = self.front

    def dequeue(self):
        # if queue is empty
        if self.is_empty():
            print('Queue is empty')
        # If last node
        elif self.front == self.rear:
            self.front = self.rear = None
        # If there are more nodes
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def display(self):
        """Display all the items in a Queue"""
        print("Elements in Circular Queue are: ", end=" ")

        temp = self.front
        while (temp.next != self.front):
            print(temp.data, "<-", end=" ")
            temp = temp.next
        print(temp.data)


# Driver code
if __name__ == '__main__':
    q = CircularQueue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(90)
    q.display()
    q.dequeue()
    q.display()
