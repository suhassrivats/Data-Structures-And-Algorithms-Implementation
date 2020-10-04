# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """
        Time Complexity: O(N), where NN is the number of nodes in the given
        tree.
        Space Complexity: O(N)
        """

        stack, pre = [], None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if pre and pre.val != node.val:
                return False
            pre = node
            root = node.right


# Recursive
class Solution:
    def isUnivalTree(self, root):
        if not root:
            return True

        if root.left:
            if root.val != root.left.val:
                return False

        if root.right:
            if root.val != root.right.val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
