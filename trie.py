class Node:
    def __init__(self):
        self.children = {}  # mapping from character to Node
        self.value = None


def insert(node, key, value=0):
    """Insert key into node."""
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
    prefix: string
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
    """Find node by key. Returning the found node itself."""
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node
