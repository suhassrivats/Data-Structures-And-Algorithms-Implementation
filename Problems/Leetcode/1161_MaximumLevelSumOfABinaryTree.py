import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative - BFS
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_level_sum, max_level, level = float('-inf'), 0, 0
        q = collections.deque()
        q.append(root)  # (node, level)

        while q:
            level_sum = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_level_sum < level_sum:
                max_level_sum, max_level = level_sum, level

        return max_level


# Recursive - BFS
class Solution:
    def __init__(self):
        self.levels = {}

    def maxLevelSum(self, root: TreeNode) -> int:
        self.sum_vals(root, 1, self.levels)
        return max(self.levels, key=self.levels.get)

    def sum_vals(self, node, depth, levels):
        if not node:
            return None
        levels[depth] = levels.get(depth, 0) + node.val
        self.sum_vals(node.left, depth+1, levels)
        self.sum_vals(node.right, depth+1, levels)
        return levels
