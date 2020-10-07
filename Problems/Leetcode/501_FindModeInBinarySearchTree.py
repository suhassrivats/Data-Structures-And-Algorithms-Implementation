# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        number_frequency = {}
        results = []
        self.dfs(root, number_frequency)
        if len(number_frequency) == 0:
            return results
        max_num_freq = max(number_frequency.values())
        for num, freq in number_frequency.items():
            if freq == max_num_freq:
                results.append(num)
        return results

    def dfs(self, root, number_frequency):
        if not root:
            return
        number_frequency[root.val] = number_frequency.get(root.val, 0) + 1
        self.dfs(root.left, number_frequency)
        self.dfs(root.right, number_frequency)
