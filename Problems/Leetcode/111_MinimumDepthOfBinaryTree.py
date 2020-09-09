from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        Explanation: LC102
        """
        if not root:
            return 0

        queue = deque([root])
        min_depth = 0

        while queue:
            min_depth += 1
            cur_level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    # Check if this is a leaf node
                    if not node.left and not node.right:
                        return min_depth

                    # insert children of current node into the queue
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
