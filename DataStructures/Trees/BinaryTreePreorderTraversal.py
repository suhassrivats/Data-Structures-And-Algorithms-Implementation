# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        root -> left -> right
        """
        results = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                results.append(node.val)
                # Stack is a LIFO and we need to traverse left before right. We
                # push right before left so that we can access left first.
                # ex: [root, right, left], pop will give us left.
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return results


# Recursive
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
