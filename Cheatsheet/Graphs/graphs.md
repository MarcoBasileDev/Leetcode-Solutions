# Graphs

A graph is a data structure composed of nodes (vertices) connected by edges. Graphs are used to model relationships, where the edges define the connections between nodes.

Below is the implementation of the GraphNode class:

```python
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
```

---

## Terminology

- **Adjacent node/neighbor**: Two nodes are adjacent if there's an edge connecting them.
- **Degree**: The number of edges connected to a node.
- **Path**: A sequence of nodes connected by edges.

---

## Attributes

- **Directed vs. Undirected**: In a directed graph, edges have a direction associated with them.
- **Weighted vs. Unweighted**: In a weighted graph, edges have an assigned weight, such as distance or cost.
- **Cyclic vs. Acyclic**: A cyclic graph contains at least one cycle, which is a path that starts and ends at the same node.

---

## Representations

In some problems, the graph may not be given directly, requiring you to create your own representation. The two most common ways to represent graphs are:

1. **Adjacency List**:

   - Stores the neighbors of each node as a list.
   - Typically implemented using a hash map, where the key represents the node and the value is a list of its neighbors.
   - Efficient for representing **sparse** graphs and for iterating over neighbors.

2. **Adjacency Matrix**:
   - Uses a 2D matrix where `matrix[i][j]` indicates an edge between nodes `i` and `j`.
   - Preferred for **dense** graphs and when frequent edge existence checks are needed.

Adjacency lists are the most common choice in practical implementations.

---

## Traversals

The primary graph traversal techniques are **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**, both of which are also used in tree traversal.

When traversing a graph, it's often necessary to keep track of visited nodes using a data structure such as a hash set to ensure each node is visited only once.

DFS is typically implemented recursively, as demonstrated in the code snippet below:

```python
def dfs(node: GraphNode, visited: Set[GraphNode]):
    visited.add(node)
    process(node)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

BFS is tipically implemented iteratively, as demonstrated in the code snippet below:

```python
def bfs(node: GraphNode):
    visited = set()
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            process(node)
            for neighbor in node.neighbors:
                queue.append(neighbor)
```

- **Time complexity**: \( O(n + e) \), where:
  - \( n \) is the number of nodes.
  - \( e \) is the number of edges.
  - Each node is visited once, and each edge is explored once.
- **Space complexity**: \( O(n) \)
  - DFS: Due to the recursive call stack.
  - BFS: Due to the queue storing nodes to be visited.
