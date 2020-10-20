# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Intuition:
        If root1 and root2 have the same root value, then we only need to check
    if their children are equal (up to ordering.)

    Algorithm:
    There are 3 cases:
    - If root1 or root2 is null, then they are equivalent if and only if they
        are both null.
    - Else, if root1 and root2 have different values, they aren't equivalent.
    - Else, let's check whether the children of root1 are equivalent to the
    children of root2. There are two different ways to pair these children.

    Time Complexity:
        O(min(N_1, N_2)), where N_1, N_2 are the lengths of root1 and root2.

    Space Complexity:
        O(min(H_1, H_2)), where H_1, H_2 are the heights of the trees of root1
        and root2.
    """

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
