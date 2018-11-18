import itertools

_THRESHOLD = 64


def merge_sort(arr, lo, hi):
    if hi - lo <= _THRESHOLD:
        _insert_sort(arr, lo, hi)
        return
    mi = (lo + hi) // 2
    merge_sort(arr, lo, mi)
    merge_sort(arr, mi, hi)
    _merge(arr, lo, mi,  hi)


def _insert_sort(arr, lo, hi):
    for i in range(lo, hi):
        for j in range(i, lo, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


def _merge(arr, lo, mi, hi):
    res = []
    index1 = lo
    index2 = mi
    while index1 < mi and index2 < hi:
        if arr[index1] <= arr[index2]:
            res.append(arr[index1])
            index1 += 1
        else:
            res.append(arr[index2])
            index2 += 1
    res += itertools.islice(arr, index1, mi)
    res += itertools.islice(arr, index2, hi)
    arr[lo: hi] = res


def _test():
    arr = [1, 0, -1, -2, -3, -2, 1, 1, 2, 1, 10, 0]
    merge_sort(arr, 0, len(arr))
    print(arr)


if __name__ == '__main__':
    _test()
