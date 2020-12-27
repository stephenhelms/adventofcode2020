from functools import reduce
import itertools as it
from pathlib import Path
import re
from typing import Iterable, List, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    cmds = parse_program(DATASET.read_text())
    print('Problem 1: ', run_program_v1(cmds))
    print('Problem 2: ', run_program_v2(cmds))


def parse_program(text: str) -> List[Tuple[str, int, int]]:
    mask_pattern = re.compile(r'mask = ([01X]{36})')
    cmd_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
    cmds = []
    mask = None
    for line in text.splitlines(False):
        mask_match = mask_pattern.match(line)
        if mask_match:
            mask = mask_match.group(1)
        else:
            mem_pos, value = cmd_pattern.match(line).groups()
            cmds.append((mask, int(mem_pos), int(value)))
    return cmds


def run_program_v1(commands: List[Tuple[str, int, int]]):
    memory = {}
    for mask, pos, value in commands:
        memory[pos] = apply_bitmask_v1(mask, value)
    return sum(memory.values())


def apply_bitmask_v1(mask: str, value: int) -> int:
    for idx, mask_value in enumerate(reversed(mask)):
        if mask_value == 'X':
            continue
        value = set_bit(value, idx, mask_value == '1')
    return value


def run_program_v2(commands: List[Tuple[str, int, int]]):
    memory = {}
    for mask, pos, value in commands:
        for mem_pos in apply_bitmask_v2(mask, pos):
            memory[mem_pos] = value
    return sum(memory.values())


def apply_bitmask_v2(mask: str, value: int) -> Iterable[int]:
    floating_bits = []
    for idx, mask_value in enumerate(reversed(mask)):
        if mask_value == '0':
            continue
        elif mask_value == '1':
            value = set_bit(value, idx, True)
        else:
            floating_bits.append(idx)
    yield reduce(lambda value, bit: set_bit(value, bit, False), floating_bits, value)
    for num_true_bits in range(1, len(floating_bits) + 1):
        for true_bits in it.combinations(floating_bits, num_true_bits):
            floating_value = value
            for bit in floating_bits:
                floating_value = set_bit(floating_value, bit, bit in true_bits)
            yield floating_value


def set_bit(value: int, bit: int, enabled: bool) -> int:
    bitmask = 1 << bit
    value &= ~bitmask
    if enabled:
        value |= bitmask
    return value


if __name__ == '__main__':
    main()
