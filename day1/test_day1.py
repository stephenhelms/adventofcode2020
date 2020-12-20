from problem import DATASET, find_entries_with_sum, read_dataset, solve_problem

EXPENSES = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_day1_problem1_solve():
    assert solve_problem(EXPENSES, 2) == 514579


def test_day1_problem2_solve():
    assert solve_problem(EXPENSES, 3) == 241861950


def test_read_dataset():
    values = read_dataset(DATASET)
    assert all(isinstance(value, int) for value in values)
    assert len(values) == 200


def test_day1_problem1_find_entries():
    assert find_entries_with_sum(EXPENSES, 2, 2020) == (1721, 299)


def test_day1_problem2_find_entries():
    assert find_entries_with_sum(EXPENSES, 3, 2020) == (979, 366, 675)
