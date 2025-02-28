# Stacks

Two main operations:

- Push (adds an element to the top of the stack).
- Pop (removes and returns the element at the top of the stack).

---

## LIFO (Last-In-First-Out)

Stacks follow the LIFO principle, meaning the most recently added item item is the first to be removed.

Stacks are useful in scenarios where the order of processing or removal is critical.

- Handling nested structure: good option for parsing or validating nested structures such as nested parentheses in a string. Allow us to process the innermost nested structures first due to the LIFO principle.
- Reverse order: when elements are added (pushed) onto a stack and then removed (popped), they come out in the reverse order of how they were added. Useful for reversing sequences.
- Substitute for recursion: we can often implement recursive functions iteratively using a stack.
- Monotonic stacks: These special-purpose stacks maintain elements in a consistent, increasing or decreasing sorted order. Before adding a new element to the stack, any elements that break this order are removed from the top of the stack, ensuring the stack remains sorted.

---

## Time Complexity Breakdown

| Operation | Worst case | Description                                                      |
| --------- | ---------- | ---------------------------------------------------------------- |
| Push      | O(1)       | Adds an element to the top of the stack.                         |
| Pop       | O(1)       | Removes and returns the element at the top of the stack.         |
| Peek      | O(1)       | Returns the element at the top of the stack without removing it. |
| IsEmpty   | O(1)       | Checks if the stack is empty.                                    |
