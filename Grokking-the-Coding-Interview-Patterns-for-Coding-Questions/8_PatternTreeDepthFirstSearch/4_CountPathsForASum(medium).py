'''
Problem Statement 
Given a binary tree and a number ‘S’, 
find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

To solve this problem, we need to find all paths in a binary tree that sum up to a given value S.
A path can start or end at any node, but it must follow the parent-to-child direction.

Here's how we can implement this:

Approach:
Use Depth-First Search (DFS) to traverse the tree.
At each node, maintain a running list of all path sums ending at that node.
For every node, check how many sub-paths (ending at that node) sum up to S.
Recurse into the left and right children.
Combine results from the left and right subtrees.

'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def countPaths(root, S):
  def dfs(node, current_path):
    if not node:
      return 0

    # Add the current node's value to the path
    current_path.append(node.val)

    # Check how many sub-paths ending at this node sum to S
    path_sum, path_count = 0, 0
    for i in range(len(current_path) - 1, -1, -1):
      path_sum += current_path[i]
      if path_sum == S:
        path_count += 1

    # Recurse for left and right children
    path_count += dfs(node.left, current_path)
    path_count += dfs(node.right, current_path)

    # Backtrack: remove the current node from the path
    current_path.pop()

    return path_count

  return dfs(root, [])


# Example Usage:
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(6)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
root.right.right = TreeNode(3)

S = 12
print("Total paths with sum", S, ":", countPaths(root, S))




'''
Time complexity 
The time complexity of the above algorithm is O(N^2) in the worst case, where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once, but for every node, we iterate the current path. 
The current path, in the worst case, can be O(N) (in the case of a skewed tree). 
But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., O(logN). 
So the best case of our algorithm will be O(NlogN).

Space complexity 
The space complexity of the above algorithm will be O(N). This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
We also need O(N) space for storing the currentPath in the worst case.
Overall space complexity of our algorithm is O(N).
'''