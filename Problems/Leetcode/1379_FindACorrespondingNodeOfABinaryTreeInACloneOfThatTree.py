# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned:
            return None
        stack = []
        stack.append((original, cloned))
        while stack:
            orig, clone = stack.pop()
            if orig == target:
                return clone
            if orig.right:
                stack.append((orig.right, clone.right))
            if orig.left:
                stack.append((orig.left, clone.left))
