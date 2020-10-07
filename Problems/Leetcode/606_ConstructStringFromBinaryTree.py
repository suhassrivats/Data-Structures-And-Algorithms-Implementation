# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive-1
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        """
        Time complexity : O(n). The preorder traversal is done over the n nodes
            of the given Binary Tree.

        Space complexity : O(n). The depth of the recursion tree can go upto n
            in case of a skewed tree.
        """

        if t is None:
            return ""

        ans = str(t.val)

        if t.left:
            ans += "(" + self.tree2str(t.left) + ")"

        if not t.left and t.right:
            ans += "()"

        if t.right:
            ans += "(" + self.tree2str(t.right) + ")"

        return ans


# Recursive-2
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        """
        Time complexity : O(n). The preorder traversal is done over the n nodes
            of the given Binary Tree.

        Space complexity : O(n). The depth of the recursion tree can go upto n
            in case of a skewed tree.
        """

        if not t:
            return ""

        if not t.left and not t.right:
            return str(t.val)

        left_string = self.tree2str(t.left)
        right_string = self.tree2str(t.right)

        # Input: Binary tree: [1,2,3,4]; Output: "1(2(4))(3)"
        # Originallay it needs to be "1(2(4)())(3()())", but you need to omit all
        # the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)".
        if right_string == "":
            return str(t.val)+"("+left_string+")"
        else:
            # we can't omit the first parenthesis pair to break the one-to-one
            # mapping relationship between the input and the output.
            # Input: Binary tree: [1,2,3,null,4]; Output: "1(2()(4))(3)"
            return str(t.val)+"("+left_string+")"+"("+right_string+")"
