import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive - using BitWise trick
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


# Recursive - DFS approach
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, pre):
        if not root:
            return 0
        pre = pre*2 + root.val
        if not root.left and not root.right:
            return pre
        return self.dfs(root.left, pre) + self.dfs(root.right, pre)


# Iterative
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        deque = collections.deque()
        results = 0
        deque.append((root, 0))
        while deque:
            node, path = deque.popleft()
            if node:
                if not node.left and not node.right:
                    results += path*2 + node.val
                path = path*2 + node.val
                deque.append((node.left, path))
                deque.append((node.right, path))
        return results
