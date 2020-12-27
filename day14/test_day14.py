import pytest

from problem import apply_bitmask, parse_program, run_program

PROGRAM = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0\
"""


@pytest.mark.parametrize('mask', ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'])
@pytest.mark.parametrize('value,result', [
    (11, 73),
    (101, 101),
    (0, 64),
])
def test_apply_bitmask(mask, value, result):
    assert apply_bitmask(mask, value) == result


def test_day14_run_program():
    cmds = parse_program(PROGRAM)
    assert run_program(cmds) == 165
