class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is
        invalid, return -1.
        """

        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        temp = self.head
        for i in range(index):
            temp = temp.next

        return temp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked
        list.
        """
        new_node = Node(val)

        # If there are no nodes in a linkedlist, then new node is head-node
        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        temp = self.head

        if self.head is None:
            self.head = new_node
        else:
            while(temp.next):
                temp = temp.next
            # Insert the new node at tail
            temp.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than the
        length, the node will not be inserted.
        """
        new_node = Node(val)
        temp = self.head

        if index < 0 or index > self.size:
            return

        # Insert the node at head (index==0)
        if index == 0:
            self.addAtHead(val)
        else:
            # Get the index of previous node
            for i in range(index - 1):
                temp = temp.next

            # At this point, temp is pointing to the previous node. Get the
            # index of current node so that we can place newnode in between
            # prev & curr
            curr_node = temp.next

            # Insert a node at a specific index
            temp.next = new_node
            new_node.next = curr_node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.size:
            return

        temp = self.head

        # If the index is the head node
        if index == 0:
            self.head = temp.next

        else:
            # Find the previous node of the node to be deleted
            for i in range(index-1):
                temp = temp.next

            # Find the next node of the node to be deleted
            next_node = temp.next.next

            # Unlink the node to be deleted
            temp.next = None
            temp.next = next_node

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(0)
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(2,2)
# obj.deleteAtIndex(1)
