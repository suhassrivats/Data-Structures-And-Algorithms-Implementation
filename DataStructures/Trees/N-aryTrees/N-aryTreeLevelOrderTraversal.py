from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Iterative
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        results = []
        queue = deque([root])

        while len(queue) > 0:
            level_result = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.children:
                    for child in node.children:
                        queue.append(child)
                level_result.append(node.val)
            results.append(level_result)
        return results
