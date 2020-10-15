# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Complexity Analysis:
        Time Complexity: O(N), where N is the number of nodes in the tree. We
            process each node once.
        Space Complexity: O(H), where H is the height of the tree. This
            represents the size of the implicit call stack in our recursion.
    """

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # If it is a leaf node and its value is 0, then set it as None
        if not root.left and not root.right and root.val == 0:
            return None

        return root
