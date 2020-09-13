# Implementation of Linked List in Python


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        last = self.head

        while(last.next):
            last = last.next

        last.next = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)
        temp = self.head

        if self.head is None:
            self.head = new_node

        # Insert at the head position
        if position == 0:
            new_node.next = self.head
            self.head = new_node

        # Get the position of a previous node
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        # Check if the position is greater than the number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Get the position of the current node
        cur_node = temp.next

        # Insert a node at a specific position
        temp.next = new_node
        new_node.next = cur_node

    def delete_node_at_pos(self, position):
        # Check if the list is empty
        if self.head == None:
            return None

        # Store a head node in a variable
        temp = self.head

        # If position is zero or it is a head-node
        if position == 0:
            self.head = temp.next
            temp = None
            return None

        # Find the previous node of the node to be deleted
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        # If position is greater than number of nodes then return none
        if temp is None:
            return
        if temp.next is None:
            return

        # Find the next node of the node to be deleted
        next_node = temp.next.next

        # Unlink the node to be deleted
        temp.next = None
        temp.next = next_node

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_rev():
        pass

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# Driver function
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(4)

ll.head.next = second
second.next = third


ll.insert_at_beginning(0)
ll.insert_after(second, 3)
ll.insert_at_end(5)
ll.insert_at_end(6)

print('Original List:')
ll.print_list()

print('Modified List:')
ll.insert_at_position(3, 10)
ll.print_list()


# ll.reverse()
# print('Reversed List:')
# ll.print_list()

# ll.delete_node_at_pos(0)
# print('After deleting a node of a given position')
# ll.print_list()
