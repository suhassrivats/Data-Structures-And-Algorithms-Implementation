class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation
        is successful.
        """
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.isFull():
            return False
        else:
            # next position of rear
            self.rear = (self.rear+1) % self.capacity
        # append from rear end
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation
        is successful.
        """
        if self.isEmpty():
            return False
        # When there is only one element
        elif self.rear == self.front:
            self.rear = self.front = -1
        else:
            # remove from front end
            self.front = (self.front+1) % self.capacity
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.rear == self.front == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if ((self.rear+1) % self.capacity) == self.front:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
