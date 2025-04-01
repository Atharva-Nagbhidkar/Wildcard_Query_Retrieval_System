from words_list import words

# B-Tree Node
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

# B-Tree Class
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t = t  

    # Insert a key into the B-Tree
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    # Insert a key in a non-full node
    def insert_non_full(self, node, k):
        if node.leaf:
            node.keys.append(k)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)

    # Split a full child
    def split_child(self, parent, i):
        t = self.t
        child = parent.children[i]
        new_child = BTreeNode(leaf=child.leaf)
        parent.keys.insert(i, child.keys[t - 1])
        parent.children.insert(i + 1, new_child)
        new_child.keys = child.keys[t:(2 * t - 1)]
        child.keys = child.keys[:t - 1]
        if not child.leaf:
            new_child.children = child.children[t:(2 * t)]
            child.children = child.children[:t]

    # Retrieve all keys with a given prefix
    def search_prefix(self, prefix):
        result = []
        self._search_prefix(self.root, prefix, result)
        return result

    def _search_prefix(self, node, prefix, result):
        for key in node.keys:
            if key.startswith(prefix):
                result.append(key)
        if not node.leaf:
            for child in node.children:
                self._search_prefix(child, prefix, result)

# Two B-Trees
btree_fwd = BTree(t=2)  # Forward B-Tree
btree_rev = BTree(t=2)  # Reverse B-Tree

# Insert words into both trees
for word in words:
    btree_fwd.insert(word)          # Normal word
    btree_rev.insert(word[::-1])    # Reversed word

# Wildcard Query Processing
def process_wildcard_query(query):
    prefix, suffix = query.split('*')

    # Step 1: Search forward B-Tree for prefix matches
    print(f"\nSearching forward B-Tree for prefix '{prefix}*'...")
    possible_matches_fwd = btree_fwd.search_prefix(prefix)
    print(f"Forward Matches: {possible_matches_fwd}\n")

    # Step 2: Search reverse B-Tree for suffix matches
    print(f"Searching reverse B-Tree for suffix '*{suffix}'...")
    possible_matches_rev = [word[::-1] for word in btree_rev.search_prefix(suffix[::-1])]
    print(f"Reverse Matches: {possible_matches_rev}\n")

    # Step 3: Find intersection of both results
    final_matches = list(set(possible_matches_fwd) & set(possible_matches_rev))
    print(f"Final Matches for query '{query}' after intersection: {final_matches}\n")
    return final_matches

# Example Query
query = "*ic"
matches = process_wildcard_query(query)