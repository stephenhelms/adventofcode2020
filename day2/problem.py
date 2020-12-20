from pathlib import Path
import re
from typing import List, NamedTuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    passwords = read_dataset(DATASET)
    print('Problem 1: ', solve_problem(passwords))


class Password(NamedTuple):
    min_occurs: int
    max_occurs: int
    letter: str
    password: str


def read_dataset(filename: Path) -> List[Password]:
    passwords = []
    with filename.open() as f:
        for line in f:
            match = re.match(r'^(\d*)-(\d*) (\w): (\w*)$', line)
            if not match:
                raise ValueError(f'Could not parse: {line}')
            passwords.append(
                Password(int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))
            )
    return passwords


def solve_problem(passwords: List[Password]) -> int:
    return sum(1 for password in passwords if validate_password(password))


def validate_password(password: Password) -> bool:
    char_count = sum(1 for char in password.password if char == password.letter)
    if password.min_occurs <= char_count <= password.max_occurs:
        return True
    return False


if __name__ == '__main__':
    main()
