# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach 1: Recursive Inorder Traversal
    It's a very straightforward approach with O(N) time complexity. The idea is
to build an inorder traversal of BST which is an array sorted in the ascending
order. Now the answer is the k - 1th element of this array.

Complexity Analysis:
Time complexity: O(N) to build a traversal.
Space complexity: O(N) to keep an inorder traversal.

Below method is optimization on approach-1.
"""


# Recursive - Inorder Traversal
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


# Iterative - Inorder Traversal
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
