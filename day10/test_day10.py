from problem import build_longest_chain, count_possible_chains, get_device_jolts, parse_adapters, solve_problem1

ADAPTERS = """\
16
10
15
5
1
11
7
19
6
12
4\
"""


def test_day10_get_device_jolts():
    adapters = parse_adapters(ADAPTERS)
    assert get_device_jolts(adapters) == 22


def test_day10_solve_problem1():
    adapters = parse_adapters(ADAPTERS)
    chain = build_longest_chain(adapters)
    assert solve_problem1(chain) == 7 * 5


def test_day10_count_possible_chains():
    adapters = parse_adapters(ADAPTERS)
    chain = build_longest_chain(adapters)
    assert count_possible_chains(chain) == 8
