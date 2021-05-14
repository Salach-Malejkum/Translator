class Node:
    def __init__(self):
        # Note that using a dictionary for children (as in this implementation)
        # would not by default lexicographically sort the children, which is
        # required by the lexicographic sorting in the Sorting section.
        # For lexicographic sorting, we can instead use an array of Nodes.
        self.children = {}  # mapping from character to Node
        self.value = None


def find(node, key):
    """Find value by key in node."""
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value


def insert(node, key, value=0):
    """Insert key/value pair into node."""
    for char in key:
        if char not in node.children:
            node.children[char] = Node()
        node = node.children[char]
    if node.value is not None:
        node.value += 1
    else:
        node.value = value


def keys_with_prefix(root, prefix):
    results = {}
    x = _get_node(root, prefix)
    _collect(x, list(prefix), results)
    return results


def _collect(x, prefix, results):
    """
    Append keys under node `x` matching the given prefix to `results`.
    prefix: list of characters
    """
    if x is None:
        return
    if x.value is not None:
        prefix_str = ''.join(prefix)
        results[prefix_str] = x.value
    for c in x.children:
        prefix.append(c)
        _collect(x.children[c], prefix, results)
        del prefix[-1]  # delete last character


def _get_node(node, key):
    """
    Find node by key. This is the same as the `find` function defined above,
    but returning the found node itself rather than the found node's value.
    """
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node


# trie = Node()
# insert(trie, 'foobar')
# insert(trie, 'foo')
# insert(trie, 'bar')
# insert(trie, 'foob')
# insert(trie, 'foof')
# key_dict = keys_with_prefix(trie, "foo")
# print(key_dict)
# print(max(key_dict, key=lambda k: key_dict[k]))
