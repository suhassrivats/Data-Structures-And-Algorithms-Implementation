import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive - DFS
class Solution:
    """
    Time Complexity: O(N) where N is the number of nodes
    Space Complexity: O(H) where H is the height of Binary Tree
    """

    def __init__(self):
        self.no_of_good_nodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.no_of_good_nodes

    def dfs(self, cur, val):
        if not cur:
            return 0
        if cur.val >= val:
            self.no_of_good_nodes += 1
        if cur.left:
            self.dfs(cur.left, max(cur.val, val))
        if cur.right:
            self.dfs(cur.right, max(cur.val, val))


# Iterative - BFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.no_of_good_nodes = 0
        q = collections.deque()
        q.append((root, float('-inf')))
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                self.no_of_good_nodes += 1
            if node.left:
                q.append((node.left, max(max_val, node.val)))
            if node.right:
                q.append((node.right, max(max_val, node.val)))
        return self.no_of_good_nodes
