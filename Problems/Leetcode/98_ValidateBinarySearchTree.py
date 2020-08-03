# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity (auxiliary): O(n)
    """

    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, min_val, max_val):
        if root is None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        valid_left = self.helper(root.left, min_val, root.val)
        valid_right = self.helper(root.right, root.val, max_val)

        return valid_left and valid_right
