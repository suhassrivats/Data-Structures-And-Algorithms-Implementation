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


# Recursion using top-down approach (kind of preorder traversal)
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


# Recursion using bottom-up approach (kind of postorder approach)
class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Iterative solution - BFS
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
