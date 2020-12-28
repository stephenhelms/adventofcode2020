from functools import reduce
from itertools import permutations
from pathlib import Path
from typing import Callable, Dict, List, Tuple

Ticket = List[int]

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    rules, my_ticket, nearby_tickets = parse_tickets(DATASET.read_text())
    print('Problem 1: ', calculate_ticket_error_rate(rules, nearby_tickets))
    ordering = find_field_ordering(rules, nearby_tickets)
    departure_fields = [value for field, value in zip(ordering, my_ticket)
                        if field.startswith('departure')]
    assert len(departure_fields) == 6
    solution = reduce(lambda agg, v: agg * v, departure_fields)
    print('Problem 2: ', solution)


def parse_tickets(text: str) -> Tuple[Dict[str, Callable[[int], bool]], Ticket, List[Ticket]]:
    rule_lines, my_ticket_lines, nearby_ticket_lines = text.split('\n\n')
    rules = {
        line.partition(':')[0]: build_validator(line.rpartition(':')[-1])
        for line in rule_lines.splitlines(False)
    }
    my_ticket = list(map(int, my_ticket_lines.splitlines(False)[1].split(',')))
    nearby_tickets = [list(map(int, line.split(','))) for line in nearby_ticket_lines.splitlines(False)[1:]]
    return rules, my_ticket, nearby_tickets


def build_validator(rule_spec: str) -> Callable[[int], bool]:
    ranges = [tuple(map(int, values.split('-')))
              for values in rule_spec.strip().split(' or ')]

    def _validate(value: int) -> bool:
        for low, high in ranges:
            if low <= value <= high:
                return True

    return _validate


def calculate_ticket_error_rate(rules: Dict[str, Callable[[int], bool]], tickets: List[Ticket]) -> int:
    return sum(invalid_ticket_score(rules, ticket) for ticket in tickets)


def invalid_ticket_score(rules: Dict[str, Callable[[int], bool]], ticket: Ticket) -> int:
    score = 0
    for value in ticket:
        has_match = False
        for rule in rules.values():
            if rule(value):
                has_match = True
                break
        if not has_match:
            score += value
    return score


def find_field_ordering(rules: Dict[str, Callable[[int], bool]], tickets: List[Ticket]) -> List[str]:
    possible_fields = list(rules.keys())
    possibly_valid_tickets = [ticket for ticket in tickets if invalid_ticket_score(rules, ticket) == 0]
    for ordered_fields in permutations(possible_fields):
        if all(validate_ticket(rules, ordered_fields, ticket) for ticket in possibly_valid_tickets):
            return list(ordered_fields)
    raise RuntimeError('Perfect ordering not found')


def validate_ticket(rules: Dict[str, Callable[[int], bool]], ordering: List[str], ticket: Ticket) -> bool:
    return all(rules[field](value) for field, value in zip(ordering, ticket))


if __name__ == '__main__':
    main()
