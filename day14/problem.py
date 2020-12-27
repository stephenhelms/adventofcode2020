from pathlib import Path
import re
from typing import List, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    cmds = parse_program(DATASET.read_text())
    print('Problem 1: ', run_program(cmds))


def parse_program(text: str) -> List[Tuple[str, int, int]]:
    mask_pattern = re.compile(r'mask = ([01X]{36})')
    cmd_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
    cmds = []
    mask = None
    for line in text.splitlines(False):
        mask_match = mask_pattern.match(line)
        if mask_match:
            mask = mask_match.group(0)
        else:
            mem_pos, value = cmd_pattern.match(line).groups()
            cmds.append((mask, int(mem_pos), int(value)))
    return cmds


def run_program(commands: List[Tuple[str, int, int]]):
    memory = {}
    for mask, pos, value in commands:
        memory[pos] = apply_bitmask(mask, value)
    return sum(memory.values())


def apply_bitmask(mask: str, value: int) -> int:
    for idx, mask_value in enumerate(reversed(mask)):
        if mask_value == 'X':
            continue
        bitmask = 1 << idx
        value &= ~bitmask
        if mask_value == '1':
            value |= bitmask
    return value


if __name__ == '__main__':
    main()
