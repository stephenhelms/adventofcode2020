from pathlib import Path
from typing import List, Optional, Set

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    groups = parse_input(DATASET.read_text())
    print('Problem 1: ', count_total_yes_questions(groups, how='any'))
    print('Problem 2: ', count_total_yes_questions(groups, how='all'))


def parse_input(data: str) -> List[List[str]]:
    return [group.splitlines(False) for group in data.split('\n\n')]


def count_total_yes_questions(groups: List[List[str]], *, how: str) -> int:
    return sum(count_group_yes_questions(group, how=how) for group in groups)


def count_group_yes_questions(group: List[str], *, how: str) -> int:
    yes_answers: Optional[Set] = None
    for person in group:
        person_answers = {letter for letter in person}
        if yes_answers is not None and how == 'any':
            yes_answers |= person_answers
        elif yes_answers is not None and how == 'all':
            yes_answers &= person_answers
        else:
            yes_answers = person_answers
    return len(yes_answers)


if __name__ == '__main__':
    main()
