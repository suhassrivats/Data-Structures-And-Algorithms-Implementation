# Level order is Breadth First traversal
from collections import deque


"""
Time complexity:
    The time complexity of the this algorithm is O(N), where ‘N’ is the total
number of nodes in the tree. This is due to the fact that we traverse each node
once.

Space complexity:
    The space complexity of this algorithm will be O(N) as we need to
return a list containing the level order traversal. We will also need O(N)
space for the queue. Since we can have a maximum of N/2 nodes at any level
(this could happen only at the lowest level), therefore we will need O(N)
space to store them in the queue.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
