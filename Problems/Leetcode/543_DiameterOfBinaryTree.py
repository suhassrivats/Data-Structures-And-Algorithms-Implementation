# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.tree_diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Time complexity #
            The time complexity of the above algorithm is O(N), where ‘N’ is
        the total number of nodes in the tree. This is due to the fact that we
        traverse each node once.

        Space complexity:
            The space complexity of the above algorithm will be O(N) in the
        worst case. This space will be used to store the recursion stack. The
        worst case will happen when the given tree is a linked list (i.e.,
        every node has only one child).
        """

        self.calculate_height(root)
        return self.tree_diameter

    def calculate_height(self, current_node):
        if not current_node:
            return 0

        left_tree_height = self.calculate_height(current_node.left)
        right_tree_height = self.calculate_height(current_node.right)

        # update global tree_diameter
        self.tree_diameter = max(self.tree_diameter, left_tree_height+right_tree_height)

        # height of the current node will be equal to the maximum of the heights
        # of left or right subtrees plus '1' for the current node
        return max(left_tree_height + right_tree_height) + 1
