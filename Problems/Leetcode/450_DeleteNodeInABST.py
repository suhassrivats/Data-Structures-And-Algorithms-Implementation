# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        # Base Case
        if not root:
            return

        # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If the key to be delete is greater than the root's key
        # then it lies in right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If key is same as root's key, then this is the node to be deleted
        else:
            # Case 1&2: No child or one-child
            if not root.left:
                temp = root.right
                root = None
                return temp
            if not root.right:
                temp = root.left
                root = None
                return temp

            # Case 3: 2-childern. Get inorder successor (smallest in right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.val = temp.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root

    def minValueNode(self, node):
        """
        Two options to find the minValueNode.
        1) Max value from left subtree (we choose this option)
        2) Min value from right subtree
        """
        curr = node
        # loop down to find the leftmost leaf
        while curr.left:
            curr = curr.left
        return curr
