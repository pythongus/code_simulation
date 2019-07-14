"""Classic Quick Sort Alogorithm
"""
import pytest
from random import randint


def quick_sort(a_list):

    def qs(i, p, j, l):
        if i > j:
            return l
        qsort(i, p, j, l)
        qs(p + 1, len(l) - 1, len(l) - 2, l)
        qs(i, p - 1, p - 2, l)
        return l

    def qsort(i, p, j, l):
        if i > j:
            return l
        if l[i] > l[p] and i < p or l[i] < l[p] and i > p:
            l = swap(i, p, l)
            p = i
        if l[j] > l[p] and j < p or l[j] < l[p] and j > p:
            l = swap(j, p, l)
            p = j
        return qsort(i + 1, p, j - 1, l)

    if not isinstance(a_list, list):
        return None
    if len(a_list) < 2:
        return a_list
    p = len(a_list) - 1
    i = 0
    j = p - 1
    return qs(i, p, j, a_list[:])


def swap(i, j, l):
    l[i], l[j] = l[j], l[i]
    return l


@pytest.mark.swap
def test_swap():
    assert swap(0, 1, [2, 1]) == [1, 2]


def test_quick_sort_with_non_list():
    assert quick_sort("a") is None


def test_quick_sort_empty_list():
    assert quick_sort([]) == []


def test_quick_sort_one_element():
    assert quick_sort([1]) == [1]


def test_quick_sort_two_elements():
    assert quick_sort([1, 2]) == [1, 2]
    assert quick_sort([1, 1]) == [1, 1]
    assert quick_sort([2, 1]) == [1, 2]


def test_quick_sort_3_elements():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]
    assert quick_sort([1, 3, 2]) == [1, 2, 3]
    assert quick_sort([3, 2, 1]) == [1, 2, 3]
    assert quick_sort([3, 3, 3]) == [3, 3, 3]
    assert quick_sort([2, 3, 2]) == [2, 2, 3]


def test_quick_sort_4_elements():
    assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert quick_sort([1, 2, 2, 4]) == [1, 2, 2, 4]
    assert quick_sort([4, 2, 2, 4]) == [2, 2, 4, 4]
    assert quick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_quick_sort_10_random_elements():
    a_list = [randint(1, 10) for _ in range(10)]
    assert quick_sort(a_list) == sorted(a_list)


def test_quick_sort_with_10_elements():
    a_list =  [6, 4, 3, 6, 5, 10, 10, 10, 9, 5]
    assert quick_sort(a_list) == sorted(a_list)
