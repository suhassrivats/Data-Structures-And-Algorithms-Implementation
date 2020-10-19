# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Time Complexity: O(N) where N is the number of nodes. We traverse the entire
        tree
    Space Complexity: O(S + N) where S is the length of to_delete set and N is
        the number of nodes in a tree. In the worst case, it could be a skewed
        Tree. So we might have to make N calls, therefore N callstack space.
        We can argue that to_delete can't be longer than the number of nodes in
        a tree itself. In which case, space complexity will be O(N + N) => O(N)
    """

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        remaing_nodes = []
        # Add root to remaing_nodes if it is not be deleted
        if root.val not in to_delete_set:
            remaing_nodes.append(root)
        self.removeNodes(root, to_delete_set, remaing_nodes)
        return remaing_nodes

    def removeNodes(self, node, to_delete_set, remaing_nodes):
        if not node:
            return None
        node.left = self.removeNodes(node.left, to_delete_set, remaing_nodes)
        node.right = self.removeNodes(node.right, to_delete_set, remaing_nodes)

        # If a parent node needs to be deleted, make sure that its children are
        # copied
        if node.val in to_delete_set:
            if node.left:
                remaing_nodes.append(node.left)
            if node.right:
                remaing_nodes.append(node.right)
            return None

        return node
