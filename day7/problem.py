from pathlib import Path
import re
from typing import Dict, Tuple

BagRule = Dict[str, int]
BagRules = Dict[str, BagRule]

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    rules = parse_rules(DATASET.read_text())
    print('Problem 1: ', count_num_possible_containing_bags(rules, 'shiny gold'))
    print('Problem 2: ', count_num_inner_bags(rules, 'shiny gold'))


def parse_rules(text: str) -> BagRules:
    return {
        outer_bag: rule
        for outer_bag, rule
        in (parse_rule(rule_text) for rule_text in text.splitlines(False))
    }


def parse_rule(text: str) -> Tuple[str, BagRule]:
    outer_bag, contents = re.match(r'^([\w\s]+) bags contain (.+)\.$', text).groups()
    possible_inner_bags = {}
    if 'no other bags' not in text:
        for inner_bag_rule in contents.split(','):
            num_bags, inner_bag = re.match(r'(\d+) ([\w\s]+) bag', inner_bag_rule.strip()).groups()
            possible_inner_bags[inner_bag] = int(num_bags)
    return outer_bag, possible_inner_bags


def count_num_possible_containing_bags(rules: BagRules, inner_bag: str) -> int:
    return sum(1 for outer_bag in rules.keys()
               if check_outer_bag_can_contain_inner(rules, outer_bag, inner_bag))


def check_outer_bag_can_contain_inner(rules: BagRules, outer_bag: str, inner_bag: str) -> bool:
    for allowed_inner_bag in rules[outer_bag].keys():
        if allowed_inner_bag == inner_bag:
            return True
        elif check_outer_bag_can_contain_inner(rules, allowed_inner_bag, inner_bag):
            return True
    return False


def count_num_inner_bags(rules: BagRules, outer_bag: str) -> int:
    return sum(number * (1 + count_num_inner_bags(rules, inner_bag))
               for inner_bag, number in rules[outer_bag].items())


if __name__ == '__main__':
    main()
