# Prefix Sums

## What is a Prefix Sum?

A **prefix sum array** is an array where each element at index `i` stores the sum of all elements from index `0` to `i` in the original array.

### Example

Given the array:

```python
spending = [10, 15, 20, 10, 5]
```

The corresponding prefix sum array is:

```python
prefix_sums = [10, 25, 45, 55, 60]
```

### Code Implementation in Python

```python
def compute_prefix_sums(nums):
    if not nums:
        return []

    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    return prefix_sum
```

### Complexity Analysis

- **Time Complexity**: \( O(n) \) (since we iterate through the array once)
- **Space Complexity**: \( O(n) \) (for storing the prefix sum array)

## Applications of Prefix Sums

- **Efficient Subarray Sum Queries**
- **Prefix Products**: A variation where we maintain a running product instead of a sum.
