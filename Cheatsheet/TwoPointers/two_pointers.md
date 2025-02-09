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