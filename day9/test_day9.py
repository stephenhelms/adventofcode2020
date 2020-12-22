from problem import encode_weakness, find_invalid_number, find_range_with_sum, parse_code

CODE = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576\
"""


def test_day9_find_invalid_number():
    code = parse_code(CODE)
    assert find_invalid_number(code, 5) == 127


def test_day9_find_range_with_sum():
    code = parse_code(CODE)
    assert find_range_with_sum(code, 127) == [15, 25, 47, 40]


def test_day9_encode_weakness():
    assert encode_weakness([15, 25, 47, 40]) == 62

