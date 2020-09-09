from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        Explanation: LC102
        """

        if not root:
            return []

        results = []
        queue = deque([root])
        left_to_right = True

        while queue:
            cur_level = deque()
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    # Add the node to cur_level based on the direction
                    if left_to_right:
                        cur_level.append(node.val)
                    else:
                        cur_level.appendleft(node.val)

                    # Insert children of current node to queue
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            results.append(cur_level)
            # reverse the traversal direction
            left_to_right = not left_to_right

        return results
