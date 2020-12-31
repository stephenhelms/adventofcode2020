from problem import parse_initial_state, compute_next_state

INITIAL_STATE = """\
.#.
..#
###\
"""


def test_day17_parse_initial_state():
    assert parse_initial_state(INITIAL_STATE) == {
        (0, 1, 0),
        (1, 2, 0),
        (2, 0, 0),
        (2, 1, 0),
        (2, 2, 0),
    }


def test_day17_compute_next_state():
    initial_state = parse_initial_state(INITIAL_STATE)
    assert compute_next_state(initial_state) == {
        (1, 0, -1),
        (2, 2, -1),
        (3, 1, -1),
        (1, 0, 0),
        (1, 2, 0),
        (2, 1, 0),
        (2, 2, 0),
        (3, 1, 0),
        (1, 0, 1),
        (2, 2, 1),
        (3, 1, 1),
    }


def test_day17_solution_problem1():
    state = parse_initial_state(INITIAL_STATE)
    for _ in range(6):
        state = compute_next_state(state)
    assert len(state) == 112
