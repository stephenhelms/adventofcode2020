from functools import partial
from pathlib import Path
import re
from typing import Callable, Dict, Iterable, List

DATASET = Path(__file__).parent / 'dataset.txt'

def _validate_height(value: str) -> bool:
    if 'cm' in value:
        return 150 <= int(value.partition('cm')[0]) <= 193
    if 'in' in value:
        return 59 <= int(value.partition('in')[0]) <= 76
    else:
        raise ValueError(value)


VALIDATION_RULES = {
    'byr': lambda s: 1920 <= int(s) <= 2002,
    'iyr': lambda s: 2010 <= int(s) <= 2020,
    'eyr': lambda s: 2020 <= int(s) <= 2030,
    'hgt': _validate_height,
    'hcl': partial(re.match, r'#[a-f|0-9]{6}'),
    'ecl': partial(re.match, r'amb|blu|brn|gry|grn|hzl|ot'),
    'pid': partial(re.match, r'\d{9}'),
}


def main():
    passports = list(parse_dataset(DATASET.read_text()))
    print('Problem 1: ', count_valid_passports(passports, validate_passport_problem1))


def parse_dataset(dataset: str) -> Iterable[Dict[str, str]]:
    passport = {}
    for line in dataset.splitlines(False):
        if not line and passport:
            yield passport
            passport = {}
        else:
            for entry in line.split(' '):
                key, value = entry.split(':')
                passport[key] = value
    yield passport


def count_valid_passports(passports: List[Dict[str, str]], validator: Callable[[Dict[str, str]], bool]) -> int:
    return sum(validator(passport) for passport in passports)


def validate_passport_problem1(passport: Dict[str, str]) -> bool:
    return set(passport.keys()).issuperset(set(VALIDATION_RULES.keys()))


def validate_passport_problem2(passport: Dict[str, str]) -> bool:
    pass


if __name__ == '__main__':
    main()
