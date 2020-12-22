from collections import deque
from pathlib import Path
from typing import List

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    code = parse_code(DATASET.read_text())
    invalid_number = find_invalid_number(code, 25)
    print('Problem 1: ', invalid_number)
    weakness = encode_weakness(find_range_with_sum(code, invalid_number))
    print('Problem 2: ', weakness)


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


def find_range_with_sum(code: List[int], search_value: int) -> List[int]:
    for range_len in range(2, len(code)):
        sum_value = 0
        last_values = deque([0] * range_len, range_len)
        for idx, value in enumerate(code):
            sum_value -= last_values.popleft()
            sum_value += value
            last_values.append(value)

            if idx < range_len:
                continue
            if sum_value == search_value:
                return code[idx - range_len + 1:idx + 1]
    raise ValueError('Range not found')


def encode_weakness(values: List[int]) -> int:
    return min(values) + max(values)


if __name__ == '__main__':
    main()
