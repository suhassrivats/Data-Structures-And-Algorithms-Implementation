"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack, results = [root], []
        while stack:
            parent = stack.pop()
            if parent:
                results.append(parent.val)
                if parent.children:
                    # Insert the elements in reverse order so that when you pop,
                    # you pop the left most child
                    for i in range(len(parent.children)-1, -1, -1):
                        stack.append(parent.children[i])
        return results
