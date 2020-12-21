from problem import find_final_acc_value_finite_program, Program

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


def test_day8_find_final_acc_value_finite_program():
    program = Program(PROGRAM)
    assert find_final_acc_value_finite_program(program) == 8
