from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        Time complexity: O(N)
        Space complexity: O(N)
        Explanation: LC102_BinaryTreeLevelOrderTraversal
        """

        if not root:
            return []

        results = deque()
        queue = deque([root])

        while queue:
            cur_level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    cur_level.append(node.val)
            results.appendleft(cur_level)

        return results
