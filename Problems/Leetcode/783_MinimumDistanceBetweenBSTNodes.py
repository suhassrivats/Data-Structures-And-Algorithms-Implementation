# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        previous, min_diff = None, float('inf')

        # Inorder traversal gives array in an ascending order
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return min_diff
            node = stack.pop()
            if previous:
                min_diff = min(min_diff, node.val-previous.val)
            previous = node
            root = node.right
