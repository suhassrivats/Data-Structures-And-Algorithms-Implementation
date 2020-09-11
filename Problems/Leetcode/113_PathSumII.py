# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        all_paths = []
        self.dfs(root, sum, current_path)
        return all_paths

    def dfs(self, root, sum, current_path, all_paths):
        if (root.val == sum) and (not root.left and not root.right):
            current_path.append(root.val)
            all_paths.append(current_path)
        if root.left:
            self.dfs(root.left, sum-root.val, current_path+[root.val], all_paths)
        if root.right:
            self.dfs(root.right, sum-root.val, current_path+[root.val], all_paths)


# Iterative
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return []

        all_paths = []
        stack = [(root, [root.val])]
        while stack:
            node, current_path = stack.pop()
            if (sum(current_path) == s) and (not node.left and not node.right):
                all_paths.append(current_path)
            if node.right:
                stack.append((node.right, current_path+[node.right.val]))
            if node.left:
                stack.append((node.left, current_path+[node.left.val]))

        return all_paths
