# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        """
        Complexity: Time O(N!), Space O(N!).
        """
        # If N is even, then there can't be a FBT
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        result = []
        for i in range(1, N, 2):
            # For each subtree that has the number of N nodes, possible left
            # subtree could have the number of [1, 3, 5, ..., N -1]. Once we have
            # the number (i) of left subtree, we can know the corresponding number
            # (N - 1 - i) of right subtree. Then, we just combine all the left
            # subtrees from self.allPossibleFBT(i) with all the right subtrees
            # self.allPossibleFBT(N - 1 - i).
            left_trees = self.allPossibleFBT(i)
            right_trees = self.allPossibleFBT(N-1-i)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result.append(root)
        return result


class Solution:
    """
    Better Solution: Recursion + Memoization
    Explanations: Based on the naive solution, we can use a dictionary to record different N.
    Complexity: Time O(2^N), Space O(2^N).
    """

    def __init__(self):
        self.memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N not in self.memo:
            res = []
            for i in range(1, N, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - 1 - i):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            self.memo[N] = res
        return self.memo[N]
