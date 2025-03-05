# Heaps

A heap is a data structure that organizes elements based on priority, ensuring the highest-priority element is always at the top of the heap. This allows for efficient access to the highest-priority element at any time. A heap is essentially a binary tree.

- Min-Heap: prioritizes the smallest element by keeping it at the top of the heap.
- Max-Heap: prioritizes the largest element by keeping it at the top of the heap.

---

## Time Complexity Breakdown

| Operation | Time Complexity | Description                                                                                        |
| --------- | --------------- | -------------------------------------------------------------------------------------------------- |
| Insert    | O(log(n))       | Adds an element to the heap, ensuring the binary tree remains correctly ordered.                   |
| Deletion  | O(log(n))       | Removes the element at the top of the heap, then restructures the heap to replace the top element. |
| Peek      | O(1)            | Retrieves the top element of the heap without removing it.                                         |
| Heapify   | O(n)            | Transform an unsorted list of values into a heap.                                                  |

---

## Priority queue

A priority queue is a special type of heap that follows the structure of min-heaps or max-heaps but allows customization in how elements are prioritized (e.g. prioritizing strings with a higher number of vowels.)
