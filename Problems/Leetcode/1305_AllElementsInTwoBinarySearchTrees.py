from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        results = []
        list1 = deque(self.inorderTraversal(root1))
        list2 = deque(self.inorderTraversal(root2))

        while list1 and list2:
            if list1[0] < list2[0]:
                results.append(list1.popleft())
            else:
                results.append(list2.popleft())
        return results + list(list1) + list(list2)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
