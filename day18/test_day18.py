import pytest

from problem import eval_expression, find_subexpressions


@pytest.mark.parametrize('expression,result', [
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
])
def test_day18_eval_expression(expression, result):
    assert eval_expression(expression) == result


@pytest.mark.parametrize('expression,results', [
    ('1 + 2 * 3 + 4 * 5 + 6', []),
    ('1 + (2 * 3) + (4 * (5 + 6))', ['(2 * 3)', '(5 + 6)']),
])
def test_day18_find_subexpression(expression, results):
    assert list(find_subexpressions(expression)) == results
