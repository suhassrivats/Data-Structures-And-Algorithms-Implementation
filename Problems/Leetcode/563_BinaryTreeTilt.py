# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        return self.dfs(root)[1]

    def dfs(self, root):  # return (sum, tilt)
        if not root:
            return (0, 0)
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return (l[0]+root.val+r[0], l[1]+r[1]+abs(l[0]-r[0]))


# Example:
    #             4
    #     2               9
    # 3       5               7

# Tree:
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(9)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(7)
#
# Tracing:
# 3: (3, 0)
# 5: (5, 0)
# 2: (10, 2)
# 7: (7, 0)
# 9: (16, 7)
# 4: (26, 2+7+7=16)
