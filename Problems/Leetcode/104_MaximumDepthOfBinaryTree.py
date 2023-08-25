from collections import deque
"""
Time complexity: O(N), N is the number of nodes. Becasue we use DFS/BFS to
traverse all the nodes.
Space complexity: O(N), N is the number of nodes. Becasue the stack may
potentially store all the nodes.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive - DFS (inorder) approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative - DFS (preorder) approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res

# Recursive - DFS (preorder) approach
class Solution:

    def __init__(self):
        self.answer = 0

    def maxDepth(self, root: TreeNode, depth=1) -> int:
        if root is None or root == []:
            return 0

        if root.left == None and root.right == None:
            self.answer = max(self.answer, depth)

        self.maxDepth(root.left, depth+1)
        self.maxDepth(root.right, depth+1)

        return self.answer

# Iterative - BFS approach
class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            cur, val = queue.popleft()
            if cur.left:
                queue.append((cur.left, val+1))
            if cur.right:
                queue.append((cur.right, val+1))

        return val
