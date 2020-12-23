from dataclasses import dataclass
import math
from pathlib import Path
from typing import List, NamedTuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    commands = parse_commands(DATASET.read_text())
    state = ShipState(0, 0, 0)
    for command in commands:
        state = command.execute(state)
    print('Problem 1: ', state.manhattan_distance)


@dataclass
class ShipState:
    x: int
    y: int
    orientation: int

    @property
    def manhattan_distance(self) -> int:
        return abs(self.x) + abs(self.y)


class Command(NamedTuple):
    action: str
    value: int

    def execute(self, state: ShipState) -> ShipState:
        if self.action == 'N':
            return ShipState(state.x, state.y + self.value, state.orientation)
        elif self.action == 'S':
            return ShipState(state.x, state.y - self.value, state.orientation)
        elif self.action == 'E':
            return ShipState(state.x + self.value, state.y, state.orientation)
        elif self.action == 'W':
            return ShipState(state.x - self.value, state.y, state.orientation)
        elif self.action == 'L':
            return ShipState(state.x, state.y, self._wrap_angle(state.orientation + self.value))
        elif self.action == 'R':
            return ShipState(state.x, state.y, self._wrap_angle(state.orientation - self.value))
        elif self.action == 'F':
            return ShipState(
                round(state.x + math.cos(state.orientation * 2 * math.pi / 360) * self.value),
                round(state.y + math.sin(state.orientation * 2 * math.pi / 360) * self.value),
                state.orientation
            )
        else:
            raise ValueError(f'Unknown action: {self.action}')

    @staticmethod
    def _wrap_angle(angle: int) -> int:
        if angle < 0:
            return 360 + angle
        elif angle > 360:
            return angle - 360
        else:
            return angle


def parse_commands(text: str) -> List[Command]:
    return [
        Command(line[0], int(line[1:]))
        for line in text.splitlines(False)
    ]


if __name__ == '__main__':
    main()
