# Breadth First Search (BFS) Pattern

Any problem involving the traversal of a tree in a **level-by-level order** can be efficiently solved using this approach. We use a **Queue** to keep track of all the nodes of a level before we jump onto the next level.

This also means the space complexity of the algorithm will be:

```
O(W)
```

where **W** is the maximum number of nodes on any level.

---

# When to Use DFS (Breadth First Search)

Look for these signals in a problem statement:

* "Traverse tree **level by level**"
* "Find the **minimum depth** / **maximum depth** of a tree"
* "Find all **nodes at distance K** from the root"
* "**Zigzag** / spiral order traversal"
* "**Connect nodes** at the same level (siblings)"
* "Find the **level averages** in a binary tree"
* "**Right view** / left view of a binary tree"
* "Find the **successor/predecessor** of a given node in level order"

If the problem cares about **which level** a node belongs to, or requires processing nodes **level-by-level**, BFS is the right tool.

---

# Algorithm Steps

1. Start by pushing the root node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, first count the elements in the queue (call it `levelSize`). We will have this many nodes in the current level.
4. Next, remove `levelSize` nodes from the queue and push their value into an array to represent the current level.
5. After removing each node from the queue, insert both of its children into the queue.
6. If the queue is not empty, repeat from step 3 for the next level.

---

# Example Code

```python
from collections import deque

def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        currentLevel = []

        for _ in range(levelSize):
            node = queue.popleft()
            currentLevel.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(currentLevel)

    return result
```

---

# Time & Space Complexity

Time complexity:

```
O(N)
```

every node is visited once.

Space complexity:

```
O(W)
```

where W is the maximum number of nodes on any single level (the widest level of the tree).

---

# Problems in This Folder

| # | Problem | Difficulty |
|---|---------|------------|
| 1 | Binary Tree Level Order Traversal | Easy |
| 2 | Reverse Level Order Traversal | Easy |
| 3 | Zigzag Traversal | Medium |
| 4 | Level Averages in a Binary Tree | Easy |
| 5 | Minimum Depth of a Binary Tree | Easy |
| 6 | Level Order Successor | Easy |
| 7 | Connect Level Order Siblings | Medium |
| 8 | Connect All Level Order Siblings | Medium |
| 9 | Right View of a Binary Tree | Easy |
