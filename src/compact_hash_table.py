from collections import abc


class CompactHashTable(abc.MutableMapping):
    def __init__(self, initial_capacity=16):
        self._buckets = [None for _ in range(initial_capacity)]
        self._max_skip = None
        self._update_max_skip()
        self._size = 0

    def __getitem__(self, item):
        index = self._get_index(item)
        if index == -1:
            raise KeyError(item)
        else:
            return self._buckets[index][1]

    def __setitem__(self, key, value):
        index = self._get_index(key)
        if index == -1:
            slot = self._find_slot(key)
            if slot == -1:
                self._resize()
                slot = self._find_slot(key)
                if slot == -1:
                    raise TooManyCollisionsError()
                else:
                    self._buckets[slot] = (key, value)
                    self._size += 1
            else:
                self._buckets[slot] = (key, value)
                self._size += 1
        else:
            self._buckets[index] = (key, value)

    def __len__(self):
        return self._size

    def __contains__(self, item):
        index = self._get_index(item)
        return index != -1

    def __iter__(self):
        return (i for i in self._buckets if i is not None)

    def __delitem__(self, key):
        index = self._get_index(key)
        if index == -1:
            raise KeyError(key)
        else:
            self._buckets[index] = None
            self._size -= 1

    def clear(self):
        for i in range(len(self._buckets)):
            self._buckets[i] = None
        self._size = 0

    def _resize(self):
        prev = self._buckets
        self._buckets = [None for _ in range(2 * len(prev))]
        self._update_max_skip()
        for entry in prev:
            if entry is None:
                continue
            slot = self._find_slot(entry[0])
            if slot == -1:
                raise TooManyCollisionsError()
            else:
                self._buckets[slot] = entry

    def _find_slot(self, key):
        start = hash(key) % len(self._buckets)
        for i in range(self._max_skip):
            index = (start + i * i) % len(self._buckets)
            entry = self._buckets[index]
            if entry is None:
                return index
        return -1

    def _get_index(self, key) -> int:
        start = hash(key) % len(self._buckets)
        for i in range(self._max_skip):
            index = (start + i * i) % len(self._buckets)
            entry = self._buckets[index]
            if entry is None:
                continue
            if entry[0] == key:
                return index
        return -1

    def _update_max_skip(self):
        self._max_skip = (len(self._buckets) // 2) + 1


class TooManyCollisionsError(Exception):
    pass


def _test():
    hashtable = CompactHashTable(4)
    assert len(hashtable) == 0
    assert 1 not in hashtable
    hashtable[1] = '1'
    assert len(hashtable) == 1
    assert hashtable[1] == '1'
    hashtable.clear()
    for i in range(16):
        assert len(hashtable) == i
        hashtable[i] = str(i)
    for i in range(16):
        assert hashtable[i] == str(i)
    for i in range(16):
        assert len(hashtable) == 16 - i
        del hashtable[i]
        assert i not in hashtable


if __name__ == '__main__':
    _test()
