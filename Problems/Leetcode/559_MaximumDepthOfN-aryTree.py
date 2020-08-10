from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Iterative - BFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        else:
            queue = []
            queue.append((root, 1))
            depth = 0
            for (node, level) in queue:
                depth = level
                queue += [(child, level+1) for child in node.children]
            return depth
