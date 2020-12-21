from itertools import tee
from pathlib import Path

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    codes = DATASET.read_text().splitlines(False)
    seat_ids = [code_to_seat_id(code) for code in codes]
    highest_seat_id = max(seat_ids)
    print('Problem 1: ', highest_seat_id)
    missing_seat_id = next(id + 1 for id, next_id in pairwise(sorted(seat_ids))
                           if next_id - id > 1)
    print('Problem 2: ', missing_seat_id)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def code_to_seat_id(code: str) -> int:
    row = decode_row(code)
    seat = decode_seat(code)
    return encode_id(row, seat)


def decode_row(code: str) -> int:
    row_code = code[:-3]
    return _parse_binary_code(row_code, 'B')


def decode_seat(code: str) -> int:
    seat_code = code[-3:]
    return _parse_binary_code(seat_code, 'R')


def _parse_binary_code(code, high_bit_letter):
    value = 0
    for bit_idx, letter in enumerate(reversed(code)):
        mask = 1 << bit_idx
        value &= ~mask
        if letter == high_bit_letter:
            value |= mask
    return value


def encode_id(row: int, seat: int) -> int:
    return row * 8 + seat


if __name__ == '__main__':
    main()
