from pathlib import Path
from typing import Callable, Dict, List, Tuple

Ticket = List[int]

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    rules, my_ticket, nearby_tickets = parse_tickets(DATASET.read_text())
    print('Problem 1: ', calculate_ticket_error_rate(rules, nearby_tickets))


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


if __name__ == '__main__':
    main()
