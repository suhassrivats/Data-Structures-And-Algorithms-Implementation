# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """
        Time Complexity: O(N), where NN is the total number of nodes in the
            given tree. We visit each node at most once.

        Space Complexity: O(N). Even though we don't explicitly use any
            additional memory, the call stack of our recursion could be as
            large as the number of nodes in the worst case.
        """
        if not root:
            return None

        # If the value of this node is less than L, then the whole left subtree
        # will be smaller, so we can discard the left sub tree and return the
        # root of the trimmed right sub tree
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # If the value of this node is greater than R, then the whole right
        # subtree will be greater so we can discard the right sub tree and return
        # the root of the trimmed left sub tree
        if (root.val > high):
            return self.trimBST(root.left, low, high)

        # If the value of this node does not need to be deleted, we need to
        # pass this recursive call downwards to both sides
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)

        return root
