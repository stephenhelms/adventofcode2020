import pytest

from problem import apply_bitmask_v1, apply_bitmask_v2, parse_program, run_program_v1, run_program_v2

PROGRAM_V1 = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0\
"""
PROGRAM_V2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1\
"""


@pytest.mark.parametrize('mask', ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'])
@pytest.mark.parametrize('value,result', [
    (11, 73),
    (101, 101),
    (0, 64),
])
def test_apply_bitmask_v1(mask, value, result):
    assert apply_bitmask_v1(mask, value) == result


def test_day14_run_program_v1():
    cmds = parse_program(PROGRAM_V1)
    assert run_program_v1(cmds) == 165


@pytest.mark.parametrize('mask,value,result', [
    ('000000000000000000000000000000X1001X', 42, {26, 27, 58, 59}),
    ('00000000000000000000000000000000X0XX', 26, {16, 17, 18, 19, 24, 25, 26, 27})
])
def test_apply_bitmask_v2(mask, value, result):
    assert set(apply_bitmask_v2(mask, value)) == result


def test_day14_run_program_v2():
    cmds = parse_program(PROGRAM_V2)
    assert run_program_v2(cmds) == 208
