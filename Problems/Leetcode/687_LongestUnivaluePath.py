# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Time Complexity:
        O(N), where N is the number of nodes in the tree. We process every node
    once.

    Space Complexity:
        O(H), where H is the height of the tree. Our recursive call stack could
    be up to H layers deep.
    """

    def __init__(self):
        self.longest = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.longest

    def dfs(self, node):
        if not node:
            return 0
        left_len = self.dfs(node.left)
        right_len = self.dfs(node.right)

        left = (left_len + 1) if node.left and node.left.val == node.val else 0
        right = (right_len + 1) if node.right and node.right.val == node.val else 0

        # since path not necessarily traverses through the root, we need to see
        # what the max is at every node level
        self.longest = max(self.longest, left+right)
        return max(left, right)
