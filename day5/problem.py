from pathlib import Path

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    codes = DATASET.read_text().splitlines(False)
    highest_seat_id = max(code_to_seat_id(code) for code in codes)
    print('Problem 1: ', highest_seat_id)


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
