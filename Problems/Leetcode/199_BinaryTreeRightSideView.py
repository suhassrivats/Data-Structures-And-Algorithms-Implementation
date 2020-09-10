from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        Approach:
            This problem follows the Binary Tree Level Order Traversal pattern.
        We can follow the same BFS approach. The only additional thing we will
        be do is to append the last node of each level to the result array.

        Time Complexity: O(N)
        Space Complexity O(N)
        Explanation: LC102_BinaryTreeLevelOrderTraversal algorithm
        """

        if not root:
            return None

        queue = deque([root])
        results = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    results.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return results
