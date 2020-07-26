"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root):
        if not root:
            return None
        q = deque()
        q.append(root)
        q.append(None)

        while q:
            node = q.popleft()
            if node is not None:
                node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if len(q) > 0:
                    q.append(None)

        return root
