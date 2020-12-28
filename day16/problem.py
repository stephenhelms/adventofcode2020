from functools import reduce
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

Ticket = List[int]

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    rules, my_ticket, nearby_tickets = parse_tickets(DATASET.read_text())
    print('Problem 1: ', calculate_ticket_error_rate(rules, nearby_tickets))
    ordering = find_field_ordering(rules, [my_ticket] + nearby_tickets)
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
    return sum(invalid_ticket_score(rules, ticket) or 0 for ticket in tickets)


def invalid_ticket_score(rules: Dict[str, Callable[[int], bool]], ticket: Ticket) -> Optional[int]:
    score = None
    for value in ticket:
        has_match = False
        for rule in rules.values():
            if rule(value):
                has_match = True
                break
        if not has_match:
            score = score or 0
            score += value
    return score


def find_field_ordering(rules: Dict[str, Callable[[int], bool]], tickets: List[Ticket]) -> List[str]:
    possibly_valid_tickets = [ticket for ticket in tickets if invalid_ticket_score(rules, ticket) is None]
    possible_fields_per_position = [
        {field for field, validator in rules.items()
         if all(validator(ticket[pos]) for ticket in possibly_valid_tickets)}
        for pos in range(len(rules))
    ]
    if any(len(fields) == 0 for fields in possible_fields_per_position):
        raise RuntimeError('Some positions have no possible fields')
    while any(len(fields) > 1 for fields in possible_fields_per_position):
        changed = False
        for pos in range(len(rules)):
            only_possible_pos_fields = {field for field in possible_fields_per_position[pos]
                                        if not any(field in fields
                                                   for other_pos, fields in enumerate(possible_fields_per_position)
                                                   if other_pos != pos)}
            if len(only_possible_pos_fields) == 1:
                print(f'Position {pos} with options {possible_fields_per_position[pos]} must be {only_possible_pos_fields} because it is the only possible position')
                possible_fields_per_position[pos] = only_possible_pos_fields
            if len(possible_fields_per_position[pos]) == 1:  # solution found
                field = next(iter(possible_fields_per_position[pos]))
                print(f'Position {pos} is {field}, it is the only remaining option')
                for other_pos in range(len(rules)):
                    if other_pos != pos:
                        possible_fields_per_position[other_pos] -= {field}
                changed = True
        if any(len(fields) == 0 for fields in possible_fields_per_position):
            raise RuntimeError('No solution found -- one position has no possible fields')
        if not changed:
            raise RuntimeError('No solution found -- cannot solve remaining fields')
    return [next(iter(fields)) for fields in possible_fields_per_position]


def validate_ticket(rules: Dict[str, Callable[[int], bool]], ordering: List[str], ticket: Ticket) -> bool:
    return all(rules[field](value) for field, value in zip(ordering, ticket))


if __name__ == '__main__':
    main()
