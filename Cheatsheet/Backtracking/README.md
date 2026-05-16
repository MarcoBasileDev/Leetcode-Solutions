# Backtracking

Imagine you're at an intersection in a maze, and only one of the three paths ahead leads to the exit. Since you're unsure which to take, you decide to explore each option one by one.

1. You start with path A and reach another intersection with two new paths, D and E.
2. You try D, but it leads to a dead end, so you backtrack.
3. Next, you try E, but it also leads to a dead end, so you backtrack again.
4. Since neither D nor E worked, you return to the first intersection.
5. You now try path B and find that it leads to the exit.

This process of exploring all possible paths, backtracking upon failure, and continuing until a valid solution is found is called **backtracking**.

---

## State Space Tree

In backtracking, the **state space tree** (also known as a decision tree) is a conceptual tree representing all possible decisions at each step.

- **Edges**: Represent possible decisions, moves, or actions.
- **Root node**: Represents the initial state before any decisions are made.
- **Intermediate nodes**: Represent partially completed states.
- **Leaf nodes**: Represent either complete solutions or dead ends.
- **Path**: A sequence of decisions from the root to a leaf node.

Visualizing the state space tree helps in understanding the algorithm and its traversal, which forms the core of backtracking.

---

## Backtracking Algorithm

Backtracking typically traverses the **state space tree** using recursive **Depth-First Search (DFS)**.

### Steps:

1. **Define the termination condition**: Specifies when a path should end (valid or invalid solution).
2. **Iterate through possible decisions** at the current state:
   - Make a decision and update the state.
   - Recursively explore all paths branching from the updated state.
   - Undo the decision (backtrack) and revert the state.

### General Template:

```python
def dfs(state):
    if meets_termination_condition(state):
        process_solution(state)
        return

    for decision in possible_decisions(state):
        make_decision(state, decision)
        dfs(state)
        undo_decision(state, decision)
```

---

## Time Complexity Analysis

The time complexity of backtracking depends on:

- **Branching factor (b)**: The number of choices available at each step.
- **Depth (d)**: The maximum number of steps needed to reach a solution.

In the worst case, every node at each level of the state space tree must be explored, leading to a time complexity of:

$$
O(b^d)
$$

where:

- b is the branching factor.
- d is the depth of the tree.

This exponential growth makes backtracking inefficient for large problem spaces unless optimized with pruning techniques.

---

## When to Use Backtracking

Backtracking is useful when we need to systematically explore all possible solutions, especially when constraints must be met. Common applications include:

- **Generating permutations, subsets, and combinations**
- **Solving constraint satisfaction problems** (e.g., Sudoku, N-Queens)
- **Path finding in mazes or puzzles**
- **Constructing valid sequences** (e.g., balanced parentheses, word formation)

By pruning invalid paths early, backtracking efficiently narrows the search space, making it a powerful tool for solving combinatorial problems.
