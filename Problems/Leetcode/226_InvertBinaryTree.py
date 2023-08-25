# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if root is None:
            return None

        # Swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Repeat the steps for root.left and root.right nodes recursively
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
