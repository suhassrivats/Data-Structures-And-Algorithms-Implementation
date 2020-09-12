# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        freq = {0: 1}
        self.dfs(root, sum, 0, freq)
        return self.count

    def dfs(self, root, sum, previous_sum, freq):
        if not root:
            return

        current_sum = previous_sum + root.val
        x = current_sum - sum
        if x in freq:
            self.count += freq[x]

        # If current_sum is already in the freq, then increase by one.
        # Else create a new current_sum
        freq[current_sum] = freq.get(current_sum, 0) + 1

        self.dfs(root.left, sum, current_sum, freq)
        self.dfs(root.right, sum, current_sum, freq)
        freq[current_sum] -= 1
