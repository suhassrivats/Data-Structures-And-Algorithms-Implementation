# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root = TreeNode(max(nums))
        left, right = self.break_array(root.val, nums)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root

    def break_array(self, num, nums):
        if nums == []:
            return ([], [])
        index = nums.index(num)
        return nums[:index], nums[index+1:]
