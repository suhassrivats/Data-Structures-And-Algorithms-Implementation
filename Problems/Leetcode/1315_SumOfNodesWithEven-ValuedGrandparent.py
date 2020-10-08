import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative - BFS
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # Since we are only concerned about EvenValued grandparents and root has
        # no parents or grandparents, we can assume that root's grandparents is 1
        queue = collections.deque([(root, 1)])  # (node, value of parent)
        result = 0
        while queue:
            node, parent_val = queue.popleft()
            if node:
                for child in [node.left, node.right]:
                    if child:
                        if parent_val % 2 == 0:
                            result += child.val
                        queue.append((child, node.val))
        return result


class Solution:
    def __init__(self):
        self.total = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root, 1, 1)
        return self.total

    def dfs(self, node, parent_val, grandparent_val):
        if node is None:
            return
        if grandparent_val % 2 == 0:
            self.total += node.val
        self.dfs(node.left, node.val, parent_val)
        self.dfs(node.right, node.val, parent_val)
