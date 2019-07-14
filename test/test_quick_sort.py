"""Classic Quick Sort Alogorithm

Test module for Quick Sort.
"""
from random import randint
import pytest
from sorting.quick_sort import quick_sort, swap


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
    a_list = [6, 4, 3, 6, 5, 10, 10, 10, 9, 5]
    assert quick_sort(a_list) == sorted(a_list)
