import pytest

from problem import count_group_yes_questions, count_total_yes_questions, parse_input

EXAMPLE_INPUT = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


@pytest.fixture
def parsed_input():
    groups = parse_input(EXAMPLE_INPUT)
    assert len(groups) == 5
    return groups


def test_day5_count_num_yes_questions(parsed_input):
    counts = [count_group_yes_questions(group) for group in parsed_input]
    assert counts == [3, 3, 3, 1, 1]


def test_day5_count_total_yes_questions(parsed_input):
    assert count_total_yes_questions(parsed_input) == 11
