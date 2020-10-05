# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative - Preorder traversal
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack, total = [(root, False)], 0
        while stack:
            node, is_left = stack.pop()
            if node:
                if not node.left and not node.right and is_left:
                    total += node.val
                stack.append((node.right, False))
                stack.append((node.left, True))
        return total


# Recursive
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root, False)

    def dfs(self, root, is_left):
        if not root:
            return 0
        if not root.left and not root.right and is_left:
            return root.val
        return self.dfs(root.left, True) + self.dfs(root.right, False)
