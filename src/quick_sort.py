def quick_sort(arr, lo, hi):
    if hi - lo <= 1:
        return
    mi = _partition(arr, lo, hi)
    quick_sort(arr, lo, mi)
    quick_sort(arr, mi + 1, hi)


def _partition(arr, lo, hi):
    pivot = arr[lo]
    while hi - 1 > lo:
        while hi - 1 > lo and arr[hi - 1] >= pivot:
            hi -= 1
        arr[lo] = arr[hi - 1]
        while hi - 1 > lo and arr[lo] <= pivot:
            lo += 1
        arr[hi - 1] = arr[lo]
    arr[lo] = pivot
    return lo


def _test():
    arr = [-2, 1, 0, 0, 1, 1, 1, 2, 3, -2]
    quick_sort(arr, 0, len(arr))
    print(arr)


if __name__ == '__main__':
    _test()
