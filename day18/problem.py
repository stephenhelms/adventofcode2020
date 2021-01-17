from pathlib import Path
import re
from typing import Iterable

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    expressions = DATASET.read_text().splitlines(False)
    print('Problem 1: ', sum(eval_expression(expression) for expression in expressions))


def eval_expression(expression: str) -> int:
    while '(' in expression:
        for subexpression in find_subexpressions(expression):
            expression = expression.replace(subexpression, str(eval_expression(subexpression[1:-1])))
    value = 0
    operation = '+'
    for token in expression.split(' '):
        if token in ('+', '-', '*'):
            operation = token
        else:
            next_value = int(token)
            value = eval(f'{value} {operation} {next_value}')
    return value


def find_subexpressions(expression: str) -> Iterable[str]:
    pattern = re.compile(r'\([^\(\)]+?\)')
    for match in pattern.finditer(expression):
        yield match.group(0)



if __name__ == '__main__':
    main()