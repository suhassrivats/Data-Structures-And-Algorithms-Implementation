"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Iteration is basically pre-order traversal but rather than go left, go right first then reverse its result.
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack, results = [root], []
        while stack:
            parent = stack.pop()
            if parent:
                results.append(parent.val)
                if parent.children:
                    # Insert the elements in left-right order so that when you pop,
                    # you pop the right most child
                    for i in range(len(parent.children)):
                        stack.append(parent.children[i])
        return results[::-1]
