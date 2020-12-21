from problem import Program

PROGRAM = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6\
"""


def test_day8_final_acc_value():
    program = Program(PROGRAM)
    assert program.run() == 5
