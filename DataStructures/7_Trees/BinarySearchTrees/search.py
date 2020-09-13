# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        if root is null return null
        root->val is equals to val return that node
        root->val > val search in the left subtree
        root->val < val search in the right subtree
        """

        if not root:
            return None

        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right

        return root
