from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        Explanation: LC102
        """

        if not root:
            return []

        results = []
        queue = deque([root])

        while queue:
            cur_level_total = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    cur_level_total += node.val
            results.append(cur_level_total/level_size)

        return results
