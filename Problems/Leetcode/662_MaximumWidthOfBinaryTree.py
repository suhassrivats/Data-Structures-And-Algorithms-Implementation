# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative - BFS
class Solution:
    """
    Intuition:
    The main idea with this question is we will give each node a position value.
    If we go down the left neighbor, then position -> position * 2; and if we go
    down the right neighbor, then position -> position * 2 + 1. This makes it so
    that when we look at the position values L and R of two nodes with the same
    depth, the width will be R - L + 1.

    Time Complexity: O(N) where N is the number of nodes
    Space Complexity: O(H) where H is the height of tree
    """

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        level = [(root, 1)]
        while level:
            new_level = []
            ans = max(ans, level[-1][1]-level[0][1]+1)
            for node, pos in level:
                if node.left:
                    new_level.append((node.left, pos*2))
                if node.right:
                    new_level.append((node.right, pos*2+1))
            level = new_level
        return ans
