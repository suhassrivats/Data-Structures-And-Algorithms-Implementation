# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative - DFS
class Solution:
    """
    Time complexity: O(N) since we visit all nodes once.
    Space complexity: O(N) since we need stacks to do recursion, and the
        maximum depth of the recursion is the height of the tree, which is O(N)
        in the worst case and O(log(N)) in the best case.
    """

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        stack = [(root, root.val, root.val)]  # (node, curr_min, curr_max)

        while stack:
            node, curr_min, curr_max = stack.pop()
            curr_min = min(node.val, curr_min)
            curr_max = max(node.val, curr_max)

            for child in [node.left, node.right]:
                if child:
                    stack.append(child, curr_min, curr_max)
            if not node.left and not node.right:
                result = max(result, curr_max-curr_min)

        return result


# Recursive - DFS
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root, root.val, root.val)

    def helper(self, node, curr_min, curr_max):
        if not node:
            return curr_max - curr_min
        curr_max = max(curr_max, node.val)
        curr_min = max(curr_min, node.val)

        left = self.helper(node.left, curr_min, curr_max)
        right = self.helper(node.right, curr_min, curr_max)

        return max(left, right)
