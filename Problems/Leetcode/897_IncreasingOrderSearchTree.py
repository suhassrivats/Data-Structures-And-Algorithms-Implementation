# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        results = self.inorder(root)
        head = TreeNode(results[0])
        current = head
        for i in range(1, len(results)):
            current.right = TreeNode(results[i])
            current = current.right
        return head

    def inorder(self, root):
        results, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                results.append(node.val)
                root = node.right
        return results
