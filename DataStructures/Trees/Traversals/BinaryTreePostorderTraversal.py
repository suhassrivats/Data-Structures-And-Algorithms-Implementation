# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# I found out that pre-order traversal is root-left-right, and post order is
# left-right-root. I modified the code for pre-order a little to make it
# root-right-left, and then reverse the output.

# Iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        left -> right -> root
        """
        results = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                results.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return results[::-1]


# Recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
