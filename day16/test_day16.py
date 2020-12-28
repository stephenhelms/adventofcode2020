import pytest

from problem import build_validator, calculate_ticket_error_rate, find_field_ordering, invalid_ticket_score,\
    parse_tickets, validate_ticket

EXAMPLE_TICKETS = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12\
"""


def test_day16_ticket_error_rate():
    rules, my_ticket, nearby_tickets = parse_tickets(EXAMPLE_TICKETS)
    assert calculate_ticket_error_rate(rules, nearby_tickets) == 71


def test_day16_build_validator():
    rule = '1-3 or 5-7'
    validator = build_validator(rule)
    assert validator(1)
    assert validator(3)
    assert not validator(4)
    assert validator(5)
    assert validator(6)
    assert not validator(8)


@pytest.mark.parametrize('ticket,expected_value', [
    ([7, 3, 47], 0),
    ([40, 4, 50], 4),
    ([55, 2, 20], 55),
    ([38, 6, 12], 12),
])
def test_day16_invalid_ticket_value(ticket, expected_value):
    rules, my_ticket, nearby_tickets = parse_tickets(EXAMPLE_TICKETS)
    assert invalid_ticket_score(rules, ticket) == expected_value


def test_day16_validate_ticket():
    rules, my_ticket, nearby_tickets = parse_tickets(EXAMPLE_TICKETS)
    assert validate_ticket(rules, ['row', 'class', 'seat'], nearby_tickets[0])


def test_day16_find_field_ordering():
    rules, my_ticket, nearby_tickets = parse_tickets(EXAMPLE_TICKETS)
    assert find_field_ordering(rules, nearby_tickets) == ['row', 'class', 'seat']
