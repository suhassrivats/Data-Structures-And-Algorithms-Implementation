# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
class Solution:
    """
    Time complexity: O(N), where N is a number of nodes, since one has to visit
        each node.
    Space complexity: up to O(H) to keep the recursion stack, where H is a tree
        height.
    """

    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.helper(root, 0)

    def helper(self, root, total):
        if not root:
            return 0
        total = (total << 1) + root.val
        if not root.left and not root.right:
            return total
        return self.helper(root.left, total) + self.helper(root.right, total)
