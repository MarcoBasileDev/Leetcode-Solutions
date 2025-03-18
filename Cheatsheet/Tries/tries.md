# **Tries (Prefix Trees)**

A **Trie** (pronounced "try") is a **tree-like** data structure that efficiently stores and retrieves **strings** by leveraging shared prefixes.

## **How Tries Work**

Instead of storing words independently, **tries group words by their prefixes**, reducing redundancy.

For example, storing "internet" and "interface":

- Both words **share the "inter" prefix**.
- The remaining characters **branch out from 'r'**.

---

## **TrieNode Structure**

Each **TrieNode** contains:

1. **Children**: A **hash map** (`{char: TrieNode}`) storing child nodes.
   - Alternatively, an **array of size 26** can be used for **lowercase English letters**.
2. **End of Word Indicator**:
   - A **boolean flag** (`is_word`) to mark the end of a valid word.
   - A **string variable** (`word`) to store the complete word at that node.

---

## **Trie Structure**

- The **root node** is an **empty node** that serves as the starting point for all words.
- Words **branch out** from the root based on their **prefixes**.

---

## **Operations & Time Complexity**

| Operation         | Time Complexity | Description                                       |
| ----------------- | --------------- | ------------------------------------------------- |
| **Insert**        | **O(k)**        | Add a word with length **k** to the trie.         |
| **Search**        | **O(k)**        | Check if a word exists in the trie.               |
| **Prefix Search** | **O(k)**        | Determine if any word starts with a given prefix. |
| **Delete**        | **O(k)**        | Remove a word from the trie.                      |

---

## **When to Use Tries**

Tries are ideal for:

- **Efficient prefix searching** (e.g., autocomplete, dictionary lookups).
- **Word validation** (e.g., spell checkers).
- **Reducing storage redundancy** by sharing common prefixes.

They are **not ideal** when:

- **Space is a concern** (tries can consume more memory than hash-based approaches).
- **Data lacks common prefixes**, making the trie structure inefficient.

---

## **Conclusion**

Tries are **powerful for text-based applications** where **prefix searches and fast lookups** are required. By leveraging **shared prefixes**, they optimize both **storage and retrieval** times compared to other data structures.
