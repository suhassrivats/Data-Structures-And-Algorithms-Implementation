# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Intuition:
        Let min1 = root.val. When traversing the tree at some node, if
    node.val > min1, we know all values in the subtree at node are at least
    node.val, so there cannot be a better candidate for the second minimum in
    this subtree. Thus, we do not need to search this subtree.

    Time Complexity: O(N), where N is the total number of nodes in the given
        tree. We visit each node at most once.

    Space Complexity: O(N). The information stored in ans and min1 is O(1), but
    our depth-first search may store up to O(h)=O(N) information in the call
    stack, where hh is the height of the tree.
    """

    def __init__(self):
        self.ans = float('inf')

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min1 = root.val
        self.dfs(root, min1)
        if self.ans < float('inf'):
            return self.ans
        else:
            return -1

    def dfs(self, node, min1):
        if not node:
            return None
        if min1 < node.val < self.ans:
            self.ans = node.val
        elif node.val == min1:
            self.dfs(node.left, min1)
            self.dfs(node.right, min1)
