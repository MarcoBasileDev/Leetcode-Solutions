# Trees

A **tree** is a hierarchical data structure composed of nodes, where each node connects to one or more child nodes. Each node in a tree contains the data it stores (`val`) and references to its child nodes.

The most common type of tree is a **binary tree**, in which each node connects to at most two children: a left child and a right child.

## Terminology

- **Parent**: a node with one or more children.
- **Child**: a node that has a parent.
- **Subtree**: a tree formed by a node and its descendants.
- **Path**: a continuous sequence of nodes connected by edges.
- **Depth**: the number of edges from the root to a given node.

## Attributes of a Tree

- **Root**: the topmost node of the tree and the only node without a parent.
- **Intermediate node**: a node with a parent and at least one child.
- **Leaf**: a node with no children.
- **Edge**: the connection between two nodes. Trees usually have directed edges, meaning edges point only from parent to child.
- **Height**: the length of the longest path from the root to a leaf.

## Tree Traversals

### Depth-First Search (DFS)

**Depth-First Search (DFS)** explores all nodes of a tree by starting at the root and moving as far down a branch as possible before backtracking to explore other branches.

DFS is typically implemented **recursively**.

```python
def dfs(node: TreeNode):
    if node is None:
        return
    process(node)
    dfs(node.left)
    dfs(node.right)
```

There are three common DFS traversal orders:

| **Preorder Traversal** (Root → Left → Right)           | **Inorder Traversal** (Left → Root → Right)            | **Postorder Traversal** (Left → Right → Root)          |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| process(node) <br> dfs(node.left) <br> dfs(node.right) | dfs(node.left) <br> process(node) <br> dfs(node.right) | dfs(node.left) <br> dfs(node.right) <br> process(node) |

#### When to Use Each DFS Traversal:

- **Preorder**: Useful when the root node needs to be processed before its children (e.g., copying a tree).
- **Inorder**: Used when nodes need to be processed in order (e.g., traversing a binary search tree in ascending order).
- **Postorder**: Important when child nodes must be processed before their parent (e.g., deleting a tree).

### Breadth-First Search (BFS)

**Breadth-First Search (BFS)** traverses the tree **level by level**, processing all nodes at the current depth before moving to the next level.  
It is typically implemented **iteratively** using a queue.

BFS is commonly used when finding the shortest path to a specific node or when processing nodes level by level (**level-order traversal**).

```Python
def bfs(root: TreeNode):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        process(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## Complexity Breakdown

Let `n` be the number of nodes and `h` be the height of the tree.

| Operation | Time Complexity | Space Complexity | Description                                                                                                                                                                                                                                                                                                            |
| --------- | --------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DFS**   | O(n)            | O(h)             | DFS visits each node once, leading to **O(n)** time complexity. The space complexity is determined by the maximum recursion depth, which corresponds to the tree height (`h`). In the worst case, when the tree is skewed (like a linked list), `h = n`. In a balanced tree, the height is approximately **O(log n)**. |
| **BFS**   | O(n)            | O(n)             | BFS visits each node once, resulting in **O(n)** time complexity. The space complexity depends on the maximum number of nodes stored in the queue at any time. In the worst case, the queue can hold all nodes at the last level, which can be up to `n/2`.                                                            |
