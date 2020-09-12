# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.global_max_sum = float('-inf')
        self.find_max_path_sum_recursive(root)
        return self.global_max_sum

    def find_max_path_sum_recursive(self, current_node):
        if not current_node:
            return 0

        max_path_sum_from_left = self.find_max_path_sum_recursive(current_node.left)
        max_path_sum_from_right = self.find_max_path_sum_recursive(current_node.right)

        # ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        max_path_sum_from_right = max(max_path_sum_from_right, 0)

        # maximum path sum at the current node will be equal to the sum from the left subtree +
        # the sum from right subtree + val of current node
        local_max_sum = max_path_sum_from_left + max_path_sum_from_right + current_node.val

        # update global_max_sum
        self.global_max_sum = max(self.global_max_sum, local_max_sum)

        # maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return max(max_path_sum_from_left, max_path_sum_from_right) + current_node.val
