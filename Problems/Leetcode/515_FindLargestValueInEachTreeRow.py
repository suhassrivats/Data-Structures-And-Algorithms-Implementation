# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        self.level_vals = {}
        self.dfs(root, 0)
        return self.level_vals.values()

    def dfs(self, node, level):
        if not node:
            return
        if level in self.level_vals:
            self.level_vals[level] = max(node.val, self.level_vals[level])
        else:
            self.level_vals[level] = node.val
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)
