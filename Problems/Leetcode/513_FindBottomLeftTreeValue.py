# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        queue = [root]
        for node in queue:
            if node.right:
                queue += [node.right]
            if node.left:
                queue += [node.left]
        return node.val
