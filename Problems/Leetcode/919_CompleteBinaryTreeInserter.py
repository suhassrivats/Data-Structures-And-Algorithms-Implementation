import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class CBTInserter:
    """
    Time Complexity: The preprocessing is O(N), where N is the number of nodes
        in the tree. Each insertion operation thereafter is O(1).
    Space Complexity: O(N_cur), when the size of the tree during the current
    insertion operation is N_cur.
    """

    def __init__(self, root: TreeNode):
        # Collect all the nodes in a deque where there is a provision to insert
        # a new node
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            # It means that there is atleast one space either in left or right
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v: int) -> int:
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        # If the left space is empty, insert a node here to maintain the CBT
        # property
        if not node.left:
            node.left = self.deque[-1]
        # If left is occupied and right is available, then insert in right space
        # and remove the node from deque as both spaces are occupied
        if not node.right:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
