class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

# Example of a tree
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3


"""
        N1
    N2      N3
"""