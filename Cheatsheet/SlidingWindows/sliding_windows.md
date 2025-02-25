# Sliding Window

The **Sliding Window** technique is a subset of the **Two Pointers** pattern, where two pointers (typically `left` and `right`) define the bounds of a **window** in iterable data structures like arrays or strings.

### **Key Characteristics**

- The **window** represents a **subcomponent** of the data structure (e.g., a subarray or substring).
- The window **slides** across the data structure in a single direction, typically searching for a subcomponent that meets a specific requirement.
- This technique is **especially useful** when solving problems that would otherwise require **nested loops** (`O(n²) complexity or worse`). By using a sliding window, the desired subcomponent can often be found in **O(n) time**.

---

### **Terminology**

- **Expanding the window** → advancing the `right` pointer.
- **Shrinking the window** → advancing the `left` pointer.
- **Sliding the window** → advancing **both** the `left` and `right` pointers.

---

## **Types of Sliding Window Algorithms**

### **Fixed Sliding Window**

A **fixed-length** window slides across the data structure.  
This is useful when the problem requires finding a **subcomponent of a known size**.

**Key Insight:**  
If a fixed window of length `k` traverses a data structure from start to finish, it **examines all possible subcomponents** of length `k`.

**Template:**

```python
left = right = 0
while right < n:
    if right - left + 1 == fixed_window_size:
        result = process_current_window()
        left += 1  # Shrink the window
    right += 1  # Expand the window
```

### **Dynamic sliding window**

A **dynamic-length** window **expands and shrinks** as it traverses the data structure.
This technique is useful for problems that require finding **the longest or shortest subcomponent** satisfying a condition.

**Key Insight:**

- **If the window satisfies the condition**, try expanding it to see if a larger valid window exists.
- **If the condition is violated**, shrink the window until it becomes valid again.

**Template:**

```python
left = right = 0
while right < n:
    while condition_is_violated():
        left += 1  # Shrink the window

    result = process_current_window()
    right += 1  # Expand the window
```
