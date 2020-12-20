from itertools import product, tee
from pathlib import Path
from typing import List, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    expenses = read_dataset(DATASET)
    print(solve_problem1(expenses))


def read_dataset(filename: Path) -> List[int]:
    with filename.open() as f:
        return [int(value) for value in f.read().splitlines()]


def solve_problem1(expenses: List[int]) -> int:
    entry1, entry2 = find_entries_with_sum(expenses, 2020)
    return entry1 * entry2


def find_entries_with_sum(expenses: List[int], summed_value: int) -> Tuple[int, int]:
    possible_values = (value for value in expenses if value < summed_value)
    for value1, value2 in product(*tee(possible_values)):
        if value1 + value2 == summed_value:
            return value1, value2
    raise RuntimeError(f'No pair of values found that add to {summed_value}')


if __name__ == '__main__':
    main()
