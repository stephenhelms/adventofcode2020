from functools import reduce
from itertools import product, tee
from pathlib import Path
from typing import Iterable, List

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    expenses = read_dataset(DATASET)
    print('Problem 1: ', solve_problem(expenses, 2))
    print('Problem 2: ', solve_problem(expenses, 3))


def read_dataset(filename: Path) -> List[int]:
    with filename.open() as f:
        return [int(value) for value in f.read().splitlines()]


def solve_problem(expenses: List[int], num_entries: int) -> int:
    entries = find_entries_with_sum(expenses, num_entries, 2020)
    return reduce(lambda agg, v: agg * v, entries)


def find_entries_with_sum(expenses: List[int], num_entries: int, summed_value: int) -> Iterable[int]:
    possible_values = (value for value in expenses if value < summed_value)
    for values in product(*tee(possible_values, num_entries)):
        if sum(values) == summed_value:
            return values
    raise RuntimeError(f'No set of {num_entries} values found that add to {summed_value}')


if __name__ == '__main__':
    main()
