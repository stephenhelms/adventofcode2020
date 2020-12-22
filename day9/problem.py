from collections import deque
from pathlib import Path
from typing import List

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    code = parse_code(DATASET.read_text())
    print('Problem 1: ', find_invalid_number(code, 25))


def parse_code(code: str) -> List[int]:
    return [int(value) for value in code.splitlines(False)]


def find_invalid_number(code: List[int], preamble_len: int) -> int:
    possible_sums = deque([None] * preamble_len ** 2, preamble_len ** 2)
    for value_idx, value in enumerate(code):
        if value_idx > preamble_len and value not in possible_sums:
            return value

        window_values = code[max(value_idx - preamble_len, 0):value_idx]
        for prev_value in window_values:
            possible_sums.append(prev_value + value)
    raise ValueError('Invalid number not found')


if __name__ == '__main__':
    main()
