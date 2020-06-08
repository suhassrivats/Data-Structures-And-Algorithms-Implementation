# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Time Complexity: O(n)
        Space Complexity (auxiliary): O(1)
        """

        if head is None:
            return None

        # Insert additional node after every node
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next

        # Adjust the pointer for newly inserted nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Separate original linked list with the duplicate one
        curr = head
        duplicate = head.next
        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            curr = temp

        return duplicate
