# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Time Complexity: O(N^2), where NN is the number of nodes.
    Space Complexity: O(N^2).
    """

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        return self.helper(pre, 0, len(pre)-1, post, 0, len(post)-1)

    def helper(self, pre, preStart, preEnd, post, postStart, postEnd):
        # Base case
        if preStart > preEnd:
            return None
        if preStart == preEnd:
            return TreeNode(pre[preStart])

        # Recursive case
        root = TreeNode(pre[preStart])
        leftRootIndexInPre = preStart + 1
        leftRootIndexInPost = post.index(pre[leftRootIndexInPre])
        leftEndIndexInPre = leftRootIndexInPre + (leftRootIndexInPost - postStart)

        root.left = self.helper(pre, leftRootIndexInPre, leftEndIndexInPre,
                                post, postStart, leftRootIndexInPost)
        root.right = self.helper(pre, leftEndIndexInPre+1, preEnd,
                                 post, leftRootIndexInPost+1, postEnd)

        return root
