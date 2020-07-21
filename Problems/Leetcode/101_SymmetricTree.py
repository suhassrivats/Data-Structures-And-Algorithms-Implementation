# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left_tree, right_tree):
        if left_tree is None and right_tree is None:
            return True
        if left_tree is None or right_tree is None:
            return False

        if left_tree.val == right_tree.val:
            outPair = self.isMirror(left_tree.left, right_tree.right)
            inPiar = self.isMirror(left_tree.right, right_tree.left)
            return outPair and inPiar
        else:
            return False


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False

        return True
