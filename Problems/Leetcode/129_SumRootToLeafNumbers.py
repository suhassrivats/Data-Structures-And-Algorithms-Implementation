# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative: DFS + Stack
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        Time complexity:
            The time complexity of the above algorithm is O(N), where ‘N’ is
        the total number of nodes in the tree. This is due to the fact that we
        traverse each node once.

        Space complexity:
            The space complexity of the above algorithm will be O(N) in the
        worst case. This space will be used to store the recursion stack. The
        worst case will happen when the given tree is a linked list (i.e.,
        every node has only one child).
        """

        if not root:
            return 0
        stack = [(root, root.val)]
        result = 0

        while stack:
            node, value = stack.pop()
            if node:
                # If they are leaf nodes
                if not node.left and not node.right:
                    result += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))

        return result


# Recursive
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, value):
        if root:
            # If it is a leaf node
            if not root.left and not root.right:
                self.result += value*10 + root.val

            self.dfs(root.left, value*10 + root.val)
            self.dfs(root.right, value*10 + root.val)
