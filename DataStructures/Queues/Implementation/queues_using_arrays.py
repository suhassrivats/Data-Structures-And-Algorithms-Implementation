# Queue implementation using Array


class Queue:

    def __init__(self, c):
        self.capacity = int(c)
        self.rear = -1
        self.front = -1
        self.queue = []

    def is_empty(self):
        if self.rear == self.front == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.capacity - 1:
            return True
        else:
            return False

    def enqueue(self, x):
        """A method to an item to the queue"""
        if self.is_full():
            print('Queue is full')
            return
        elif self.is_empty():
            print('Queue is empty')
            self.front = self.rear = 0
        else:
            self.rear += 1
        self.queue.append(x)
        print("%s enqueued to queue" % str(x))

    def dequeue(self):
        """A method to delete an item from the queue"""
        if self.is_empty():
            return
        elif self.rear == self.front:
            print("%s deque from queue" % str(self.queue[self.rear]))
            self.rear = self.front = -1
        else:
            print("%s deque from queue" % str(self.queue[self.rear]))
            self.front += 1

    def display(self):
        """Display all the items in a Queue"""
        if self.is_empty():
            print('Queue is empty!')
        for i in range(self.front, len(self.queue)):
            print(self.queue[i], "<-", end=" ")


## Driver function ##
q = Queue(4)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(90)
q.display()
q.dequeue()
q.display()
