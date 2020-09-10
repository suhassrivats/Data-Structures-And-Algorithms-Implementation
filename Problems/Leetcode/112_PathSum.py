# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if (root.val == sum) and (root.left is None) and (root.right is None):
            return True

        return self.hasPathSum(root.left, sum-root.val) or \
            self.hasPathSum(root.right, sum-root.val)


# Iterative: DFS + Stack
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, value = stack.pop()
            if (value == sum) and (not node.left and not node.right):
                return True
            if node.right:
                stack.append((node.right, value+node.right.val))
            if node.left:
                stack.append((node.left, value+node.left.val))

        return False
