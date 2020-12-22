from itertools import tee
from pathlib import Path
from typing import List

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    adapters = parse_adapters(DATASET.read_text())
    print('Problem 1: ', solve_problem1(adapters))


def parse_adapters(text: str) -> List[int]:
    return [int(value) for value in text.splitlines(False)]


def solve_problem1(adapters: List[int]) -> int:
    device_jolts = get_device_jolts(adapters)
    chain = [0] + list(sorted(adapters)) + [device_jolts]
    differences = [v_right - v_left for v_left, v_right in pairwise(chain)]
    return sum(1 for v in differences if v == 1) * sum(1 for v in differences if v == 3)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def get_device_jolts(adapters: List[int]) -> int:
    return max(adapters) + 3


if __name__ == '__main__':
    main()
