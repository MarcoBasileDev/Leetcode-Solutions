# **Intervals**

An **interval** consists of two values: a **start point** and an **end point**. It represents a **continuous segment** on the number line, including all values between these two points. Intervals are commonly used to represent **lines, time periods, or continuous ranges of values**.

### **Interval Properties**

- **Start point** → Indicates where the interval begins.
- **End point** → Indicates where the interval ends.

### **Types of Intervals**

1. **Closed `[a, b]`** → Both the **start** and **end points** are included.
2. **Open `(a, b)`** → The **start** and **end points** are **not** included.
3. **Half-open `[a, b)` or `(a, b]`** → Either the **start** or **end** point is included, while the other is not.

---

## **Overlapping Intervals**

Two **intervals overlap** if they **share at least one common value**.  
The **central challenge** in most interval problems is **managing overlapping intervals efficiently**.  
When **identifying** or **merging overlapping intervals**, it's important to determine how the **overlap influences the desired outcome**.

---

## **Sorting Intervals**

In most **interval problems**, sorting the intervals **before processing** is **helpful**, allowing them to be handled in a structured order.

### **Sorting Criteria**

1. **Primary Sorting** → By **start point** in ascending order.
2. **Secondary Sorting** → When two or more intervals **share the same start point**, sort by their **end points** if necessary.

---

## **Separating Start and End Points**

In certain cases, it can be **useful to process start and end points separately**.  
This often involves **creating two sorted arrays**:

1. **Start points array** → Contains all start values, sorted in ascending order.
2. **End points array** → Contains all end values, sorted in ascending order.

This approach is useful in **interval scheduling problems, event processing, and sweep line algorithms**.

---

## **Interval Class Definition**

```python
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
```

This class provides a simple representation of an interval with a `start` and `end` attribute.
