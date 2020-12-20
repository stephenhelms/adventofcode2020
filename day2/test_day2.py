from problem import Constraint, DATASET, Password, read_dataset, solve_problem, validate_password

PASSWORDS = [
    Password(1, 3, 'a', 'abcde'),
    Password(1, 3, 'b', 'cdefg'),
    Password(2, 9, 'c', 'ccccccccc'),
]


def test_day2_problem1_solve():
    assert solve_problem(PASSWORDS, Constraint.problem1) == 2


def test_day2_read_dataset():
    passwords = read_dataset(DATASET)
    assert passwords[0] == Password(6, 10, 'p', 'ctpppjmdpppppp')
    assert len(passwords) == 1000


def test_day2_problem1_validate_password():
    assert validate_password(PASSWORDS[0], Constraint.problem1)
    assert not validate_password(PASSWORDS[1], Constraint.problem1)
