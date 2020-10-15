# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:
    """
    Complexity Analysis:
    N -> Total number of nodes in the tree
    Time Complexity:
        dfs: O(N)
        find: O(1)

    Space Complexity:
        HashSet: O(N)
        dfs: O(H) callstack; where H is the height of tree
    """

    def __init__(self, root: TreeNode):
        self.seen = set()
        root.val = 0
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return
        self.seen.add(node.val)
        if node.left:
            node.left.val = 2 * node.val + 1
            self.dfs(node.left)  # To recover other left nodes if they exist
        if node.right:
            node.right.val = 2 * node.val + 2
            self.dfs(node.right)

    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
