ALPHABET_SIZE = 26
FIRST_LETTER = 'a'


class TrieTree:
    def __init__(self):
        self._root = _TrieTreeNode()
        self._size = 0

    def insert(self, key: str) -> bool:
        node = self._root
        for char in key:
            index = _char2index(char)
            if node.children[index] is None:
                node.children[index] = _TrieTreeNode()
            node = node.children[index]
        if node.is_end:
            return False
        node.is_end = True
        self._size += 1
        return True

    def remove(self, key: str) -> bool:
        node = self._root
        for char in key:
            node = node.children[_char2index(char)]
            if node is None:
                return False
        if node.is_end:
            self._size -= 1
            node.is_end = False
            return True
        return False

    def search(self, key: str) -> bool:
        node = self._root
        for char in key:
            node = node.children[_char2index(char)]
            if node is None:
                return False
        return node.is_end

    def __contains__(self, item):
        return self.search(item)

    def __len__(self):
        return self._size


def _char2index(char: str):
    assert len(char) == 1
    return ord(char) - ord(FIRST_LETTER)


class _TrieTreeNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = [None for _ in range(ALPHABET_SIZE)]
        self.is_end = False


def _test():
    tree = TrieTree()
    cases = frozenset("there is a moon hovering in the sky".split())
    for case in cases:
        assert tree.insert(case)
    assert len(tree) == len(cases)
    for case in cases:
        assert case in tree
    assert len(tree) == len(cases)
    assert tree.remove("is")
    assert "is" not in tree
    assert len(tree) == len(cases) - 1


if __name__ == '__main__':
    _test()
