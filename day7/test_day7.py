import pytest

from problem import check_outer_bag_can_contain_inner, count_num_possible_containing_bags, parse_rules

RULES = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.\
"""


@pytest.fixture
def rules():
    rules_ = parse_rules(RULES)
    assert len(rules_) == 9
    assert rules_['dotted black'] == {}
    assert rules_['vibrant plum'] == {
        'faded blue': 5,
        'dotted black': 6,
    }
    return rules_


@pytest.mark.parametrize('outer_bag,is_valid', [
    ('bright white', True),
    ('muted yellow', True),
    ('dark orange', True),
    ('light red', True),
    ('shiny gold', False),
    ('dark olive', False),
    ('vibrant plum', False),
    ('faded blue', False),
    ('dotted black', False),
])
def test_day7_whether_bag_can_contain_other(rules, outer_bag, is_valid):
    inner_bag = 'shiny gold'
    assert check_outer_bag_can_contain_inner(rules, outer_bag, inner_bag) == is_valid


def test_day7_num_possible_containing_bags(rules):
    assert count_num_possible_containing_bags(rules, 'shiny gold') == 4
