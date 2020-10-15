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

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root
