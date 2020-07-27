"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        parent = root
        child_head = child = None

        # Outer loop
        while parent:
            # Inner loop to traverse a level from left to right
            while parent:
                if parent.left:
                    if child_head is None:
                        child_head = parent.left
                        child = parent.left
                    else:
                        child.next = parent.left
                        child = parent.left
                if parent.right:
                    if child_head is None:
                        child_head = parent.right
                        child = parent.right
                    else:
                        child.next = parent.right
                        child = parent.right
                parent = parent.next

            parent = child_head
            child = child_head = None

        return root
