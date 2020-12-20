from pathlib import Path
from typing import Dict, Iterable, List, Set

DATASET = Path(__file__).parent / 'dataset.txt'
REQUIRED_KEYS = {
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
}


def main():
    passports = list(parse_dataset(DATASET.read_text()))
    print('Problem 1: ', count_valid_passports(passports, REQUIRED_KEYS))


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


def count_valid_passports(passports: List[Dict[str, str]], required_keys: Set[str]) -> int:
    return sum(set(passport.keys()).issuperset(required_keys)
               for passport in passports)


if __name__ == '__main__':
    main()
