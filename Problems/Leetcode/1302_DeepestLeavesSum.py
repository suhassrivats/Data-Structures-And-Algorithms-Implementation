# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        while True:
            q_new = [x.left for x in q if x.left]
            q_new += [x.right for x in q if x.right]
            if not q_new:
                break
            q = q_new
        return sum([node.val for node in q])
