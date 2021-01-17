from pathlib import Path
import re
from typing import Iterable, Callable

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    expressions = DATASET.read_text().splitlines(False)
    print('Problem 1: ', sum(eval_expression(expression) for expression in expressions))
    print('Problem 2: ', sum(eval_expression_problem2(expression) for expression in expressions))


def eval_expression(expression: str) -> int:
    expression = _eval_subexpressions(expression, eval_expression)
    return _eval_left_to_right(expression)


def eval_expression_problem2(expression: str) -> int:
    expression = _eval_subexpressions(expression, eval_expression_problem2)
    expression = _eval_addition(expression)
    return _eval_left_to_right(expression)


def _eval_subexpressions(expression, eval_func: Callable[[str], int]) -> str:
    while '(' in expression:
        for subexpression in find_subexpressions(expression):
            expression = expression.replace(subexpression,
                                            str(eval_func(subexpression[1:-1])))
    return expression


def find_subexpressions(expression: str) -> Iterable[str]:
    pattern = re.compile(r'\([^\(\)]+?\)')
    for match in pattern.finditer(expression):
        yield match.group(0)


def _eval_addition(expression: str) -> str:
    while '+' in expression:
        for match in re.finditer(r'\d+ \+ \d+', expression):
            subexpression = match.group(0)
            expression = expression.replace(subexpression, str(eval(subexpression)), 1)
    return expression


def _eval_left_to_right(expression: str) -> int:
    value = 0
    operation = '+'
    for token in expression.split(' '):
        if token in ('+', '*'):
            operation = token
        else:
            next_value = int(token)
            value = eval(f'{value} {operation} {next_value}')
    return value


if __name__ == '__main__':
    main()
