import pytest

from problem import compute_nth_number, iter_spoken_numbers


def test_day15_iter_spoken_numbers():
    starting_seq = 0, 3, 6
    it = iter(iter_spoken_numbers(starting_seq))
    assert next(it) == 0
    assert next(it) == 3
    assert next(it) == 3
    assert next(it) == 1
    assert next(it) == 0
    assert next(it) == 4
    assert next(it) == 0


@pytest.mark.parametrize('starting_seq,value', [
    ((0, 3, 6), 436),
    ((1, 3, 2), 1),
    ((2, 1, 3), 10),
    ((1, 2, 3), 27),
    ((2, 3, 1), 78),
    ((3, 2, 1), 438),
    ((3, 1, 2), 1836),
])
def test_day15_compute_nth_number(starting_seq, value):
    assert compute_nth_number(starting_seq, 2020) == value
