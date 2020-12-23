from dataclasses import dataclass
import math
from pathlib import Path
from typing import List, NamedTuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    commands = parse_commands(DATASET.read_text())
    state = ShipState(0, 0, 0)
    for command in commands:
        state = state.execute_command(command)
    print('Problem 1: ', state.manhattan_distance)


class Command(NamedTuple):
    action: str
    value: int


@dataclass
class ShipState:
    x: int
    y: int
    orientation: int

    @property
    def manhattan_distance(self) -> int:
        return abs(self.x) + abs(self.y)

    def execute_command(self, command: Command) -> 'ShipState':
        if command.action == 'N':
            return ShipState(self.x, self.y + command.value, self.orientation)
        elif command.action == 'S':
            return ShipState(self.x, self.y - command.value, self.orientation)
        elif command.action == 'E':
            return ShipState(self.x + command.value, self.y, self.orientation)
        elif command.action == 'W':
            return ShipState(self.x - command.value, self.y, self.orientation)
        elif command.action == 'L':
            return ShipState(self.x, self.y, wrap_angle(self.orientation + command.value))
        elif command.action == 'R':
            return ShipState(self.x, self.y, wrap_angle(self.orientation - command.value))
        elif command.action == 'F':
            return ShipState(
                round(self.x + math.cos(self.orientation * 2 * math.pi / 360) * command.value),
                round(self.y + math.sin(self.orientation * 2 * math.pi / 360) * command.value),
                self.orientation
            )
        else:
            raise ValueError(f'Unknown action: {command.action}')


def parse_commands(text: str) -> List[Command]:
    return [
        Command(line[0], int(line[1:]))
        for line in text.splitlines(False)
    ]


def wrap_angle(angle: int) -> int:
    if angle < 0:
        return 360 + angle
    elif angle > 360:
        return angle - 360
    else:
        return angle


if __name__ == '__main__':
    main()
