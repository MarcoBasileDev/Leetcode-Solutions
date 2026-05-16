# **Binary Search**

Binary Search is an algorithm that searches for a value in a **sorted** dataset.

## **1. Defining the Search Space**

The **search space** encompasses all possible values that may include the value we're searching for.  
For instance, when searching for a target in a sorted array, the search space should cover the **entire array**, as the target could be anywhere within it.

## **2. Narrowing the Search Space**

Narrowing the search space involves **progressively moving the left or right pointer inward** until the search space is reduced to **one element or none**.

At each step in Binary Search, we must decide how to narrow the search space:

- **Narrow the search space toward the left** (by moving the **right pointer inward**).
- **Narrow the search space toward the right** (by moving the **left pointer inward**).

### **Using the Midpoint**

We decide whether to move the **left or right pointer** based on the value at the **middle** of the search space, represented by the **midpoint variable (`mid`)**.

The key question at each iteration is:  
**Is the value being searched for to the left or the right of the midpoint?**

#### **General Strategy:**

- If the target **is to the right** of the midpoint → **move left pointer rightward**.
- If the target **is to the left** of the midpoint → **move right pointer leftward**.

### **Narrowing the Search Space Toward the Right**

Two options:

- `left = mid + 1` → If the midpoint value is **not** the value we're searching for, exclude it.
- `left = mid` → If the midpoint value **could be** the target, keep it in the search space.

### **Narrowing the Search Space Toward the Left**

The same exclusion/inclusion logic applies:

- `right = mid - 1` → If the midpoint **is not** the value we're searching for.
- `right = mid` → If the midpoint **could be** the target.

### **Calculating the Midpoint**

The midpoint is typically calculated as:

\[
\text{mid} = \frac{\text{left} + \text{right}}{2}
\]

or in integer form:

```python
mid = (left + right) // 2
```

## **3. Choosing an Exit Condition**

Determining when the **while-loop** should terminate is crucial.  
The two main exit conditions are:

- **`left < right`** → The loop stops when `left` and `right` meet.
- **`left <= right`** → The loop continues until `left` surpasses `right`.

When using `left < right`, both pointers **converge** to a **single value** at the end of the search.  
This value is the **final candidate** in the **search space** after the algorithm completes.

## **4. Returning the Correct Value**

The **while-loop terminates** when the search space is reduced to a **final value**,  
pointed to by both `left` and `right`.  
This value represents the **answer**, assuming a valid answer exists.

---

## **Time Complexity**

The time complexity of **Binary Search** is:

\[
O(\log n)
\]

where **`n`** is the number of elements in the search space.

### **Why is it Logarithmic?**

In each iteration, the algorithm **divides the search space in half**,  
until it is reduced to **a single value** (or no value if the target is not present).  
This **halving process** at every step is a characteristic of **logarithmic behavior**.

---

### Real-World Example

**Transaction search in financial systems:** In financial systems, a binary search can be used to quickly find a transaction or record by narrowing down the search range, as the data is typically stored in order. This makes it efficient to retrieve specific entries without searching through the entire database.
