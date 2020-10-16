# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Time Complexity: O(N), where N is the number of nodes in the tree.
    Space Complexity: O(H), where H is the height of the tree.
    """

    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.moves

    def dfs(self, node):
        if not node:
            return 0
        left_coins = self.dfs(node.left)
        right_coins = self.dfs(node.right)
        self.moves += abs(left_coins) + abs(right_coins)
        return node.val-1 + left_coins + right_coins
