from problem import find_invalid_number, parse_code

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
