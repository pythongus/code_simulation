"""Bubble Sort Algorithm
"""

def bb_sort(a_list):
    """Sorts the elements in a_list in ascending order"""
    i = 0; j = 1
    last_position = len(a_list) - 1
    while i < last_position:
        a_list = swap(a_list, i, j)
        i, j = next_position(i, j, last_position)

    return a_list


def next_position(i, j, last_position):
    """Calculates the next position to swap"""
    return (i + 1, i + 2) if j == last_position else (i, j + 1)


def swap(a_list, i, j):
    """Swaps the elements of a_list in positions i and j"""
    if a_list[i] > a_list[j]:
        a_list[i], a_list[j] = a_list[j], a_list[i]
    return a_list


def test_bb_sort_3_elements():
    assert bb_sort([3, 1, 2]) == [1, 2, 3]


def test_bb_sort_4_elements_with_repetition():
    assert bb_sort([3, 4, 2, 2]) == [2, 2, 3, 4]


def test_bb_sort_3_element_with_repetition():
    assert bb_sort([1, 1, 2]) == [1, 1, 2]


def test_bb_sort_2_elements():
    assert bb_sort([2, 1]) == [1, 2]


def test_bb_sort_1_element():
    assert bb_sort([1]) == [1]


def test_bb_sort_empty_list():
    assert bb_sort([]) == []


def test_bb_sort_with_strings():
    assert bb_sort(['avocado', 'Amanda', 'amarillo', 'Aunt Z']) == \
        ['Amanda', 'Aunt Z', 'amarillo', 'avocado']
