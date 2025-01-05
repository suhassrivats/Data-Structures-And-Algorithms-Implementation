'''
Problem Statement 
Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def isValidSequence(root, sequence):
  def dfs(node, index):
    # Base case: if the node is None, return False
    if not node:
      return False

    # If index is out of bounds, return False (sequence is too long)
    if index >= len(sequence):
      return False

    # If we reach the end of the sequence, check if it's a leaf node
    if index == len(sequence) - 1:
      return node.val == sequence[index] and not node.left and not node.right
      # if node.val == sequence[index] and not node.left and not node.right:
      #   return True
      # else:
      #   return False

    # Check the current node value matches the sequence
    if node.val == sequence[index]:
      # Recursively check the left and right subtrees
      return dfs(node.left, index + 1) or dfs(node.right, index + 1)

    return False

  # Start DFS from the root and index 0 in the sequence
  return dfs(root, 0)

# Example Tree:
#       1
#      / \
#     2   3
#    / \   / \
#   4   5 6   7

# Create the tree nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Test case: sequence [1, 2, 5]
sequence = [1, 2, 5]
result = isValidSequence(root, sequence)
print(result)  # Output: True (Path: 1 → 2 → 5)

# Test case: sequence [1, 3, 7]
sequence = [1, 3, 7]
result = isValidSequence(root, sequence)
print(result)  # Output: True (Path: 1 → 3 → 7)

# Test case: sequence [1, 3, 6]
sequence = [1, 3, 6]
result = isValidSequence(root, sequence)
print(result)  # Output: True (Path: 1 → 3 → 6)

# Test case: sequence [1, 2, 4]
sequence = [1, 2, 4]
result = isValidSequence(root, sequence)
print(result)  # Output: True (Path: 1 → 2 → 4)

# Test case: sequence [1, 2, 6]
sequence = [1, 2, 6]
result = isValidSequence(root, sequence)
print(result)  # Output: False (No path matches this sequence)




'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''