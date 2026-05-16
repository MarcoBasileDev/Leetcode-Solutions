# Dynamic Programming

Some problems can be broken down into subproblems, where each subproblem is a smaller version of the main problem. These subproblems may themselves be broken down further. This is similar to recursion. However, in recursion, the same subproblem might be solved multiple times, leading to unnecessary computations.

**Dynamic Programming (DP)** is the antidote to this inefficiency. It is a technique that stores solutions to subproblems so they can be reused, ensuring each subproblem is solved at most once. This significantly improves performance.

---

## The DP Process

DP follows a structured problem-solving approach:

1. **Optimal Substructure** – The optimal solution to a problem can be built from optimal solutions to its subproblems.
2. **Overlapping Subproblems** – The same subproblems are solved multiple times during computation.
3. **Recurrence Relation** – A formula that expresses the solution in terms of smaller subproblems.
4. **Base Cases** – The simplest instances of the problem with known solutions.

The first two properties determine whether DP can be applied to a problem, while the last two are crucial for implementing a DP solution effectively.
