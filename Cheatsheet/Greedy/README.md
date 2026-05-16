# Greedy

Greedy algorithms are a class of algorithms that make a series of decisions, where each decision is the best immediate choice given the options available.

---

## How does a greedy algorithm work?

A greedy algorithm follows the greedy choice property, which states that the best overall solution to a problem (global optimum) can be arrived at by making the best possible decision at each step (local optimum). Each decision is made based only on the current context, and ignores its impact on future steps. This process continues until the algorithm reaches a final solution.

---

## How to tell if a problem can be solved using a greedy approach

Greedy approaches are generally used for optimization problems, similar to DP. This mens we check if the problem has an optimal substructure which can be broken down and solved by smaller subproblems. The key difference between DP and greedy approaches is their decision-making strategies. Greedy algorithms follow the greedy choice property , while DP considers all possible solutions to find the global optimum. It's generally the case that all greedy problems can be solved using DP, but not all DP problems can be solved using a greedy approach.
