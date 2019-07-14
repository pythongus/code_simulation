"""Classic Quick Sort Alogorithm
"""


def quick_sort(list_):
    """Classic quick sort function"""
    if not isinstance(list_, list):
        return None
    if len(list_) < 2:
        return list_
    pivot = len(list_) - 1
    i = 0
    j = pivot - 1
    return _qsort(i, pivot, j, list_[:])


def _qsort(i, pivot, j, list_):
    if i > j:
        return list_

    last_position = len(list_) - 1
    return _qsort(i, pivot - 1, pivot - 2,
                  _qsort(pivot + 1, last_position, last_position - 1,
                         _qs(i, pivot, j, list_)))


def _qs(i, pivot, j, list_):
    if i > j:
        return list_
    if (list_[i] > list_[pivot] and i < pivot or
            list_[i] < list_[pivot] and i > pivot):
        list_ = swap(i, pivot, list_)
        pivot = i
    if (list_[j] > list_[pivot] and j < pivot or
            list_[j] < list_[pivot] and j > pivot):
        list_ = swap(j, pivot, list_)
        pivot = j
    return _qs(i + 1, pivot, j - 1, list_)


def swap(i, j, list_):
    """Pythonic swap elements function"""
    list_[i], list_[j] = list_[j], list_[i]
    return list_
