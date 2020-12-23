import pytest

from problem import parse_commands, ShipState, ShipStateProblem2

COMMANDS = """\
F10
N3
F7
R90
F11\
"""

EXPECTED_STATES = [
    ShipState(10, 0, 0),
    ShipState(10, 3, 0),
    ShipState(17, 3, 0),
    ShipState(17, 3, 270),
    ShipState(17, -8, 270),
]
EXPECTED_STATES_2 = [
    ShipStateProblem2(100, 10, 10, 1),
    ShipStateProblem2(100, 10, 10, 4),
    ShipStateProblem2(170, 38, 10, 4),
    ShipStateProblem2(170, 38, 4, -10),
    ShipStateProblem2(214, -72, 4, -10)
]


@pytest.mark.parametrize('state,expected_states', [
    (ShipState(0, 0, 0), EXPECTED_STATES),
    (ShipStateProblem2(0, 0, 10, 1), EXPECTED_STATES_2),
])
def test_day11_commands_state(state, expected_states):
    for idx, (command, expected_state) in enumerate(zip(parse_commands(COMMANDS), expected_states)):
        print(idx)
        state = state.execute_command(command)
        assert state == expected_state


def test_day11_calculate_distance():
    assert ShipState(17, 8, 0).manhattan_distance == 25
