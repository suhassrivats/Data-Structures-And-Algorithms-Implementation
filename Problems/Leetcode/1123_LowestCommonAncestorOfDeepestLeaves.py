# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[1]

    def dfs(self, node):
        if not node:
            return 0, None
        h1, lca1 = self.dfs(node.left)  # (depth, node)
        h2, lca2 = self.dfs(node.right)

        if h1 == h2:
            return h1+1, node
        if h1 > h2:
            return h1+1, lca1
        if h1 < h2:
            return h2+1, lca2
