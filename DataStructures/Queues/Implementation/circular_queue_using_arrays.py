# Implement Circular Queue using Arrays


class CircularQueue:

    def __init__(self, c):
        self.capacity = c
        self.queue = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        if self.rear == self.front == -1:
            return True
        else:
            return False

    def is_full(self):
        if ((self.rear+1) % self.capacity) == self.front:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_full():
            print('Queue is full')
            return
        elif self.is_empty():
            print('Queue is empty')
            self.front = self.rear = 0
        else:
            self.rear = ((self.rear+1) % self.capacity)
        self.queue.append(item)

    def dequeue(self):
        # Condition for an empty array
        if self.is_empty():
            return
        # Condition for only one element
        elif self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.front = (self.front + 1) % self.capacity

    def display(self):

        i = self.front
        if self.is_empty():
            print('Queue is empty')
        else:
            print('Queue is:')
            while(i is not self.rear):
                print(self.queue[i])
                i = (i+1) % self.capacity
            print(self.queue[i])


## Driver function ##
q = CircularQueue(4)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(90)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
