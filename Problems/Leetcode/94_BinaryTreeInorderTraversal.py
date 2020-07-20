# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        left -> root -> right
        """
        results = []
        stack = []

        while root or stack != []:
            while root:
                stack.append(root)
                root = root.left

            # If there are no more elements to the left of a node
            root = stack.pop()
            results.append(root.val)
            root = root.right

        return results


# Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
