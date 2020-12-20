from enum import Enum
from pathlib import Path
import re
from typing import List, NamedTuple

DATASET = Path(__file__).parent / 'dataset.txt'


class Constraint(Enum):
    problem1 = 1
    problem2 = 2


def main():
    passwords = read_dataset(DATASET)
    print('Problem 1: ', solve_problem(passwords, Constraint.problem1))
    print('Problem 1: ', solve_problem(passwords, Constraint.problem2))


class Password(NamedTuple):
    constraint1: int
    constraint2: int
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


def solve_problem(passwords: List[Password], constraint_type: Constraint) -> int:
    return sum(1 for password in passwords if validate_password(password, constraint_type))


def validate_password(password: Password, constraint_type: Constraint) -> bool:
    if constraint_type == Constraint.problem1:
        char_count = sum(1 for char in password.password if char == password.letter)
        if password.constraint1 <= char_count <= password.constraint2:
            return True
        return False
    else:
        raise NotImplementedError(constraint_type)


if __name__ == '__main__':
    main()
