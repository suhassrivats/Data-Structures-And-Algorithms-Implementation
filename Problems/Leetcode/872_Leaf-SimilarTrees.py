# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive - DFS approach
class Solution:
    """
    Time Complexity: O(T1 + T2) where T1 and T2 are the lengths of the given trees.
    Space Complexity: O(T1 + T2) the space used in storing the leaf values.
    """

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.dfs(root.left) + self.dfs(root.right)


# Iterative - preorder/inorder/postorder
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)

    def getLeaves(self, root):  # preorder
        if not root:
            return []
        stack, results = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if not node.left and not node.right:
                    results.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return results

    def getLeaves2(self, root):  # inorder
        stack, ret = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ret
            node = stack.pop()
            if not node.left and not node.right:
                ret.append(node.val)
            root = node.right

    def getLeaves3(self, root):  # postorder
        stack, ret = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if not node.left and not node.right:
                    ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
