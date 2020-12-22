from itertools import tee
from pathlib import Path
from typing import List

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    adapters = parse_adapters(DATASET.read_text())
    chain = build_longest_chain(adapters)
    print('Problem 1: ', solve_problem1(chain))
    print('Problme 2: ', count_possible_chains(chain))


def parse_adapters(text: str) -> List[int]:
    return [int(value) for value in text.splitlines(False)]


def build_longest_chain(adapters: List[int]) -> List[int]:
    device_jolts = get_device_jolts(adapters)
    chain = [0] + list(sorted(adapters)) + [device_jolts]
    return chain


def get_device_jolts(adapters: List[int]) -> int:
    return max(adapters) + 3


def solve_problem1(longest_chain: List[int]) -> int:
    differences = [v_right - v_left for v_left, v_right in pairwise(longest_chain)]
    return sum(1 for v in differences if v == 1) * sum(1 for v in differences if v == 3)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def count_possible_chains(longest_chain: List[int]) -> int:
    max_jolts = 3
    edges = {}
    for idx, left_value in enumerate(longest_chain):
        possible_next_adapters = set()
        for right_value in longest_chain[idx + 1:]:
            if right_value - left_value <= max_jolts:
                possible_next_adapters.add(right_value)
            else:
                break
        edges[left_value] = possible_next_adapters
    possible_paths = {longest_chain[-1]: 1}
    for left_value in reversed(longest_chain[:-1]):
        possible_paths[left_value] = 0
        for right_value in edges[left_value]:
            possible_paths[left_value] += possible_paths[right_value]
    return possible_paths[longest_chain[0]]


if __name__ == '__main__':
    main()
