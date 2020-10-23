# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(H) => O(logn) where H is the height of the tree
    """

    def __init__(self):
        self.total_freq_map = {}

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.dfs(root)
        max_total_freq = max(self.total_freq_map.values())
        return [total for total in self.total_freq_map
                if self.total_freq_map[total] == max_total_freq]

    def dfs(self, node):
        if not node:
            return 0
        total = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.total_freq_map[total] = self.total_freq_map.get(total, 0) + 1
        return total
