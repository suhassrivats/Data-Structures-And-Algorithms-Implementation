class DoublyLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is
        invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        cur = self.head

        while index != 0:

            cur = cur.next
            index -= 1

        # self.print_linked_list()
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked
        list.
        """
        new_node = DoublyLLNode(val)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

        if self.size == 1:
            self.tail = new_node

        # trace and debug
        # self.print_linked_list()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = DoublyLLNode(val)
        new_node.prev
        if self.size == 0:
            self.addAtHead(val)
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

            # trace and debug
            # self.print_linked_list()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than the
        length, the node will not be inserted.
        """

        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = DoublyLLNode(val)
            curr = self.head
            while index-1 != 0:
                curr = curr.next
                index -= 1

            curr.next.prev = new_node
            new_node.next = curr.next

            curr.next = new_node
            new_node.prev = curr

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.size:
            return

        elif index == 0:

            if self.head.next:
                self.head.next.prev = None

            self.head = self.head.next

            self.size -= 1

            if self.size == 0:
                self.tail = None

        elif index == self.size-1:

            if self.tail.prev:
                self.tail.prev.next = None

            self.tail = self.tail.prev

            self.size -= 1

            if self.size == 0:
                self.head = None

        else:

            cur = self.head
            while index-1 != 0:

                cur = cur.next
                index -= 1

            cur.next = cur.next.next
            cur.next.prev = cur

            self.size -= 1

        # trace and debug
        # self.print_linked_list()

    def print_linked_list(self):

        cur = self.head

        while cur:
            print(f' {cur.val} -> ', end='')
            cur = cur.next

        print('\n')

        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(0)
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(2,2)
# obj.deleteAtIndex(1)
