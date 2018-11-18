class AvlTree:
    def __init__(self):
        self._root = None

    def search(self, item) -> bool:
        return _search(self._root, item)

    def insert(self, item) -> None:
        self._root = _insert(self._root, item)

    def remove(self, item) -> None:
        self._root = _remove(self._root, item)

    def __contains__(self, item):
        return self.search(item)


def _search(node, item) -> bool:
    if node is None:
        return False
    if node.item == item:
        return True
    elif node.item < item:
        return _search(node.right, item)
    else:
        return _search(node.left, item)


def _insert(node, item):
    if node is None:
        return _Node(None, item, None)
    if node.item == item:
        return node

    if node.item < item:
        node.right = _insert(node.right, item)
    else:
        node.left = _insert(node.left, item)
    _update_height(node)
    return _rebalance(node)


def _remove(node, item):
    if node is None:
        return None
    if node.item == item:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        value = _get_leftmost_item(node.right)
        node.item = value
        node.right = _remove(node.right, value)
    elif node.item < item:
        node.right = _remove(node.right, item)
    else:
        node.left = _remove(node.left, item)
    _update_height(node)
    return _rebalance(node)


def _rebalance(node):
    balance = _comp_balance(node)

    # left left
    if balance > 1 and _comp_balance(node.left) > 0:
        return _right_rotate(node)

    # right right
    if balance < -1 and _comp_balance(node.right) < 0:
        return _left_rotate(node)

    # left right
    if balance > 1 and _comp_balance(node.left) < 0:
        node.left = _left_rotate(node.left)
        return _right_rotate(node)

    # right left
    if balance < -1 and _comp_balance(node.right) > 0:
        node.right = _right_rotate(node.right)
        return _left_rotate(node)

    return node


def _update_height(node):
    node.height = 1 + max(_height(node.left), _height(node.right))


def _right_rotate(node):
    node2 = node.left
    node3 = node2.right
    node.left = node3
    node2.right = node
    _update_height(node)
    _update_height(node2)
    return node2


def _left_rotate(node):
    node2 = node.right
    node3 = node2.left
    node.right = node3
    node2.left = node
    _update_height(node)
    _update_height(node2)
    return node2


def _get_leftmost_item(node):
    while node.left is not None:
        node = node.left
    return node.item


def _height(node):
    if node is None:
        return 0
    return node.height


def _comp_balance(node):
    return _height(node.left) - _height(node.right)


class _Node:
    __slots__ = ("left", "item", "right", "height")

    def __init__(self, left, item, right):
        self.left = left
        self.item = item
        self.right = right
        self.height = 1


def _test():
    tree = AvlTree()
    assert 1 not in tree
    tree.insert(1)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    assert 1 in tree
    tree.remove(1)
    assert 1 not in tree
    tree.remove(1)
    assert 3 in tree


if __name__ == '__main__':
    _test()
