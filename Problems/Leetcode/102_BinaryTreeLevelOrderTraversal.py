from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        results = []
        queue = deque([root])

        while queue:
            cur_level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    cur_level.append(node.val)
            results.append(cur_level)

        return results


# Recursive
class Solution:
    def __init__(self):
        self.levels = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.helper(root, 0)

    def helper(self, root, level):
        if root is None:
            return []
        else:
            if level < len(self.levels):
                self.levels[level].append(root.val)
            else:
                self.levels.append([root.val])
            self.helper(root.left, level+1)
            self.helper(root.right, level+1)
        return self.levels
