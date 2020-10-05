# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        Intuition:
            - Inorder Traversal of the BST yields a sorted array.
            - Use 2 pointers and a simple while loop, to determine if the sum exists.

        Time Complexity: O(n), since we visit each node once both in inorder
            and in two pointer. Making it O(n + n) => O(n)
        Space Complexity: O(n), to store all nodes (call-stack + results)
        """

        # inorder traversal will give a sorted array
        array = self.inorderTraversal(root)

        # Apply two pointer technique on a sorted array
        left, right = 0, len(array)-1
        while left < right:
            total = array[left] + array[right]
            if total == k:
                return True
            elif total > k:
                right -= 1
            else:
                left += 1
        return False

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        left -> root -> right
        """
        results = []
        stack = []

        while root or stack != []:
            while root:
                stack.append(root)
                root = root.left

            # If there are no more elements to the left of a node
            root = stack.pop()
            results.append(root.val)
            root = root.right

        return results
