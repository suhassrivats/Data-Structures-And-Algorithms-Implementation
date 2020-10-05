import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return None

        deque, map = collections.deque(), {}
        deque.append(root)
        map[root.val] = (0, None)  # (depth, parent)

        while deque:  # BFS
            node = deque.popleft()
            depth = map[node.val][0]
            if node.left:
                deque.append(node.left)
                map[node.left.val] = (depth+1, node)
            if node.right:
                deque.append(node.right)
                map[node.right.val] = (depth+1, node)
            if x in map and y in map:
                # For nodes to be cousins they should be in the same depth and
                # their parents should be different
                return map[x][0] == map[y][0] and map[x][1] != map[y][1]
