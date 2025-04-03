# Sort and Search

When sorting and searching items in data structures, efficiency is key.

| Algorithm          | Best case      | Average case   | Worst case     | Space complexity              |
| ------------------ | -------------- | -------------- | -------------- | ----------------------------- |
| **Insertion sort** | O(n)           | O(n²)          | O(n²)          | O(1)                          |
| **Selection sort** | O(n²)          | O(n²)          | O(n²)          | O(1)                          |
| **Bubble sort**    | O(n)           | O(n²)          | O(n²)          | O(1)                          |
| **Merge sort**     | O(n log n)     | O(n log n)     | O(n log n)     | O(n)                          |
| **Quicksort**      | O(n log n)     | O(n log n)     | O(n²)          | O(log n) (avg) / O(n) (worst) |
| **Heapsort**       | O(n log n)     | O(n log n)     | O(n log n)     | O(1)                          |
| **Counting sort**  | O(n + k)       | O(n + k)       | O(n + k)       | O(n + k)                      |
| **Bucket sort**    | O(n + k)       | O(n + k)       | O(n²)          | O(n + k)                      |
| **Radix sort**     | O(d ⋅ (n + k)) | O(d ⋅ (n + k)) | O(d ⋅ (n + k)) | O(n + k)                      |

## Fundamental Concepts for Sorting Algorithms

- **Counting sort**: `k` represents the range of values in the input array.
- **Bucket sort**: `k` represents the number of buckets used.
- **Radix sort**: `k` represents the range of inputs, and `d` represents the number of digits in the maximum element.

---

### Key Sorting Properties

- **Stability**: A sorting algorithm is stable if it preserves the relative order of equal elements in the sorted output. If two elements have equal values, their order remains unchanged.
- **In-place sorting**: An in-place sorting algorithm sorts the elements within the original data structure, using only a constant amount of extra storage.
- **Comparison-based sorting**: These algorithms sort elements by comparing them pairwise, typically having a lower bound of **O(n log n)**. Non-comparison-based sorting algorithms can achieve linear time complexity but require specific assumptions about the input data.

---

### Real-Word Example

Sorting products by category: When users search for products, the platform often sorts the results based on various criteria such as lowest to highest price, highest to lowest rating, or even relevance to the search query. Efficient sorting algorithms ensure large datasets of products can be quickly arranged according to user preferences.
