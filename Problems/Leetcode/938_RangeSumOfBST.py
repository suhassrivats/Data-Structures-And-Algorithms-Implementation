# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        Time Complexity: O(N), where N is the number of nodes in the tree.
        Space Complexity: O(H), where H is the height of the tree.
        """
        if not root:
            return 0
        left = self.rangeSumBST(root.left, L, R)
        right = self.rangeSumBST(root.right, L, R)
        return left + right + (root.val if (L <= root.val <= R) else 0)

# Iterative
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         stack, ret = [], 0
#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             if not stack:
#                 return ret
#             node = stack.pop()
#             if L <= node.val <= R:
#                 ret += node.val
#             root = node.right
