# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self.preorder(root)

    def preorder(self, root):
        if not root:
            return []
        stack, results = [(root, "")], []
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                results.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+'->'))
            if node.left:
                stack.append((node.left, ls+str(node.val)+'->'))
        return results
