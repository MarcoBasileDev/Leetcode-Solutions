# Two Pointers

- Used to make comparisons.
- Useful with linear data structure (array or linked list).
- Useful with data structures with predictable dynamics (sorted array) => less time/space complexity.
- Useful when problem asks for a pair of values.

## Strategies

### Inward traversal

- Pointers starting at opposites ends and moving inward toward each other.
- Stop whne they meet/cross each other, or a condition is met.
- Ideal when we need to compare elements from different ends of a data stracture.

### Unidirectional traversal

- Both pointers start at the same end (usually the beginning) and move in the same direction.
- One pointer finds the information (usually the right) and another to keep track of information (usually the left).

### Staged traversal

- Traverse with one pointer and whne it lands on an element that meets a certain condition, we traverse with the second pointer.

---

### Real-World Example

**Garbage collection algorithms:** In memory compaction - which is a key part of garbage collection - the goal is to free up contiguous memory space by eliminating gaps left by deallocated (aka dead) objects. A two-pointer technique helps achieve this efficiently: a 'scan' pointer traverses the heap to identify live objects, while a 'free' pointer keeps track of the next available space to where live objects should be relocated. As the 'scan' pointer moves, it skips over dead objects and shifts live objects to the position indicated by the 'free' pointer, compacting the memory by grouping all live objects together and freeing up continuous blocks of memory.
