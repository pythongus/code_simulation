"""Shift Right (Cycle) Algorithm

This is the test module for this algorihtm.
Shift-rights an array by n steps.
"""
import pytest


def cycle(array, step=1):
    """Right-shifts the elements of the array in given steps"""
    size = len(array)
    if not size or step >= size and not step / size:
        return array
    counter = step
    ahead = fetch(array, 0, step)
    while counter < size + step:
        position = counter % size
        swap = fetch(array, position, step)
        array = put(array, ahead, position)
        ahead = swap
        counter += step
    
    return array


def fetch(array, position, step):
    """Fetches the elements of the array from the position to 
    position + step. If the position is beyond the arra limits,
    fetches from the beginning.
    """
    size = len(array)
    if not array or size == 1:
        return array
    return [array[pos % size]
            for pos in range(position, min(size, position + step))]


def put(array, ahead, position, step=1):
    """Puts the ahead array into array, starting from position."""
    size = len(array)
    for ind, pos in enumerate(range(position, position + len(ahead))):
        array[pos % size] = ahead[ind]
    return array

 
def test_cycle_0_elements():
    assert cycle([], 2) == []


def test_cycle_1_element():
    assert cycle([1], 2) == [1]


def test_cycle_2_elements():
    assert cycle([1, 2], 2) == [1, 2]
    assert cycle([1, 2]) == [2, 1]
    assert cycle([1, 2], 3) == [2, 1]


def test_cycle_3_elements():
    assert cycle([1, 2, 3]) == [3, 1, 2]
    assert cycle([1, 2, 3], 2) == [2, 3, 1]


def test_cycle_4_elements():
    assert cycle([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert cycle([1, 2, 3, 4], 2) == [3, 4, 1, 2]


def test_cycle_5_elements():
    assert cycle([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]
    assert cycle([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_cycle_6_elements():
    assert cycle([1, 2, 3, 4, 5, 6]) == [6, 1, 2, 3, 4, 5]
    assert cycle([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]


@pytest.mark.put
def test_put_with_2_elements():
    assert put([1, 2], [1], 1, 1) == [1, 1]


@pytest.mark.put
def test_put_with_2_elements_step_2():
    assert put([1, 2], [1, 2], 2, 2) == [1, 2]


@pytest.mark.put
def test_put_with_2_elements_step_3():
    assert put([1, 2], [1], 1, 3) == [1, 1]


@pytest.mark.put
def test_put_with_5_elements_step_3():
    assert put([1, 2, 3, 4, 5], [1, 2, 3], 3, 3) == [3, 2, 3, 1, 2] 
