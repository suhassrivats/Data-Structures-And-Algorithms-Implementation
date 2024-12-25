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

def sumNumbers(root):
  def dfs(node, current_number):
    # Base case: if the node is None, return 0
    if not node:
      return 0

    # Append the current node's value to the current number string
    current_number += str(node.val)

    # If it's a leaf node, convert the current number string to an integer
    # and return it
    if not node.left and not node.right:
      return int(current_number)

    # Recur for left and right subtrees
    left_sum = dfs(node.left, current_number)
    right_sum = dfs(node.right, current_number)

    # Return the total sum from both subtrees
    return left_sum + right_sum

  # Start the DFS from the root node with an empty string
  return dfs(root, "")

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

# Get the total sum of all path numbers
result = sumNumbers(root)
print(result)  # Output: 408 (The sum of the path numbers: 124 + 125 + 136 + 137)



'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''