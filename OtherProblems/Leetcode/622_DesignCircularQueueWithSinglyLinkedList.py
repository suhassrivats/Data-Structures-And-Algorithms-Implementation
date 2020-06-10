class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = self.temp = k
        self.front = self.rear = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation
        is successful.
        """
        # If given size is zero or if the queue has reached its capacity
        if self.size == 0:
            return False

        new_node = Node(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next

        # Point the node back to head to make it circular
        self.rear.next = self.front
        self.size -= 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation
        is successful.
        """
        if self.isEmpty():
            return False
        else:
            # If last node
            if self.rear == self.front:
                self.rear = self.front = None
            # If there are more nodes
            else:
                self.front = self.front.next
                self.rear.next = self.front
            self.size += 1

            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.front.value

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear == None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == 0
