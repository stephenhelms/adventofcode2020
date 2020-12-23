from problem import parse_commands, ShipState

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


def test_day11_commands_state():
    state = ShipState(0, 0, 0)
    for idx, (command, expected_state) in enumerate(zip(parse_commands(COMMANDS), EXPECTED_STATES)):
        print(idx)
        state = command.execute(state)
        assert state == expected_state


def test_day11_calculate_distance():
    assert ShipState(17, 8, 0).manhattan_distance == 25
