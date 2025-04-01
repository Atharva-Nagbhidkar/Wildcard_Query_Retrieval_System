
# B-Tree for Wildcard Query Retrieval in Information Retrieval System

## 📚 Project Overview
This project implements a **B-Tree** data structure optimized for **Wildcard Query Retrieval** in an **Information Retrieval System**. The B-Tree is used to efficiently store, retrieve, and search for keys that match wildcard patterns, ensuring logarithmic time complexity for query operations.

---

## 🚀 Features
- **Wildcard Query Support:** Retrieve keys matching wildcard patterns.
- **Efficient Key Insertion:** Dynamically insert keys into the B-Tree.
- **Logarithmic Search:** Fast retrieval of matching keys.
- **Node Splitting:** Automatically balances the tree by splitting full nodes.
- **Scalability:** Handles large datasets with minimal rebalancing overhead.

---

## 📝 Code Explanation

### `BTreeNode` Class
- Defines the structure of a B-Tree node.
- Attributes:
  - `keys` → Stores keys in sorted order.
  - `children` → Stores child nodes.
  - `leaf` → Indicates if the node is a leaf.

### `BTree` Class
- Manages the B-Tree operations.

#### `insert(k)`
- Inserts key `k` into the B-Tree.
- Calls `insert_non_full()` if the root is not full.
- Splits the root if it's full, creating a new root.

#### `insert_non_full(node, k)`
- Handles insertion into a non-full node.
- Finds the appropriate child and inserts the key.
- Splits the child if it’s full.

#### `split_child(parent, i)`
- Splits a full child node into two nodes.
- Promotes the middle key to the parent.

#### `search(k, node=None)`
- Searches for key `k` in the B-Tree.
- Returns the node containing `k` or `None` if not found.

#### `wildcard_search(pattern, node=None)`
- Searches for keys matching a wildcard pattern (e.g., `ab*`, `*xyz`).
- Recursively checks all possible branches and returns matching keys.

---

## 🔧 How to Run
1. **Clone the Repository**
```bash
git clone https://github.com/your-username/btree-wildcard-query.git
```

2. **Navigate to the Project Directory**
```bash
cd btree-wildcard-query
```

3. **Run the Code**
```bash
python3 main.py
```

---

## 📊 Example Usage
```python
from main import BTree

# Create a B-Tree with minimum degree t = 3
btree = BTree(3)

# Insert keys
for key in ["apple", "apply", "apples", "banana", "band", "bandana"]:
    btree.insert(key)

# Search for a wildcard pattern
results = btree.wildcard_search("app*")
print("Keys matching 'app*':", results)
```

---

## 📖 Theory Behind Wildcard Query Retrieval Using B-Trees
- **B-Trees** are self-balancing search trees that maintain sorted data and allow searches, sequential access, insertions, and deletions in logarithmic time.
- In **Wildcard Query Retrieval**, the B-Tree is used to match wildcard patterns by traversing nodes and checking for matching prefixes or suffixes.
- This method ensures efficient pattern matching, even for large datasets.

---
