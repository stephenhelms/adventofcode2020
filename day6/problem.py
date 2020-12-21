from pathlib import Path
from typing import List, Optional, Set

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    groups = parse_input(DATASET.read_text())
    print('Problem 1: ', count_total_yes_questions(groups))


def parse_input(data: str) -> List[List[str]]:
    return [group.splitlines(False) for group in data.split('\n\n')]


def count_total_yes_questions(groups: List[List[str]]) -> int:
    return sum(count_group_yes_questions(group) for group in groups)


def count_group_yes_questions(group: List[str]) -> int:
    yes_answers = set()
    for person in group:
        yes_answers |= {letter for letter in person}
    return len(yes_answers)


if __name__ == '__main__':
    main()
