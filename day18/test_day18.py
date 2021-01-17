import pytest

from problem import eval_expression, eval_expression_problem2, find_subexpressions


@pytest.mark.parametrize('expression,result', [
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
])
def test_day18_eval_expression(expression, result):
    assert eval_expression(expression) == result


@pytest.mark.parametrize('expression,result', [
    ('1 + 2 * 3 + 4 * 5 + 6', 231),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 46),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
    ('8 + 3 * ((4 * 8 * 5 * 5) + (8 * 9 * 8 + 7 * 9)) + (4 * 7) + 3 * 4', 464244)
])
def test_day18_eval_expression_problem2(expression, result):
    assert eval_expression_problem2(expression) == result


@pytest.mark.parametrize('expression,results', [
    ('1 + 2 * 3 + 4 * 5 + 6', []),
    ('1 + (2 * 3) + (4 * (5 + 6))', ['(2 * 3)', '(5 + 6)']),
])
def test_day18_find_subexpression(expression, results):
    assert list(find_subexpressions(expression)) == results
