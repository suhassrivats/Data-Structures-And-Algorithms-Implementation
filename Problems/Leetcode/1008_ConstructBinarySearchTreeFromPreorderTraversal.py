# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        Idea:
        First item in preorder list is the root to be considered.
        For next item in preorder list, there are 2 cases to consider:
            If value is less than last item in stack, it is the left child of last item.
            If value is greater than last item in stack, pop it.
                The last popped item will be the parent and the item will be the right child of the parent.

        Time Complexity: O(n), where n is the number of nodes. We are visting
            each node only once.

        Space Complexity: O(n). In the worst case it can be a skewed tree. So we
            might have to store all the elements in the stack. 
        """
        if not preorder:
            return None
        # Root is always the first element in preorder
        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            new_node = TreeNode(value)
            if value < stack[-1].val:
                stack[-1].left = new_node
                stack.append(new_node)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = new_node
                stack.append(last.right)

        return root
