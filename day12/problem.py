import math
from pathlib import Path
from typing import List, NamedTuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    commands = parse_commands(DATASET.read_text())
    for problem_idx, state in enumerate((ShipState(0, 0, 0), ShipStateProblem2(0, 0, 10, 1))):
        for command in commands:
            state = state.execute_command(command)
        print(f'Problem {problem_idx + 1}: ', state.manhattan_distance)


class Command(NamedTuple):
    action: str
    value: int


class ShipState:
    def __init__(self, x: int, y: int, orientation: int):
        self.x = x
        self.y = y
        self.orientation = orientation

    def __repr__(self):
        return ','.join(map(str, (self.x, self.y, self.orientation)))

    def __eq__(self, other):
        return (self.x, self.y, self.orientation) == (other.x, other.y, other.orientation)

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
            return ShipState(self.x, self.y, self._wrap_angle(self.orientation + command.value))
        elif command.action == 'R':
            return ShipState(self.x, self.y, self._wrap_angle(self.orientation - command.value))
        elif command.action == 'F':
            return ShipState(
                round(self.x + math.cos(self.orientation * 2 * math.pi / 360) * command.value),
                round(self.y + math.sin(self.orientation * 2 * math.pi / 360) * command.value),
                self.orientation
            )
        else:
            raise ValueError(f'Unknown action: {command.action}')

    @staticmethod
    def _wrap_angle(angle: int) -> int:
        if angle < 0:
            return 360 + angle
        elif angle > 360:
            return angle - 360
        else:
            return angle


class ShipStateProblem2(ShipState):
    def __init__(self, x: int, y: int, waypoint_x: int, waypoint_y: int):
        self.x = x
        self.y = y
        self.waypoint_x = waypoint_x
        self.waypoint_y = waypoint_y

    def __repr__(self):
        return ','.join(map(str, (self.x, self.y, self.waypoint_x, self.waypoint_y)))

    def __eq__(self, other):
        return (
                (self.x, self.y, self.waypoint_x, self.waypoint_y) ==
                (other.x, other.y, other.waypoint_x, other.waypoint_y)
        )

    @property
    def orientation(self) -> float:
        return math.atan2(self.waypoint_y, self.waypoint_x) / (2 * math.pi) * 360

    @property
    def waypoint_distance(self) -> float:
        return math.sqrt(self.waypoint_x ** 2 + self.waypoint_y ** 2)

    def execute_command(self, command: Command) -> 'ShipStateProblem2':
        if command.action == 'N':
            return ShipStateProblem2(self.x, self.y, self.waypoint_x, self.waypoint_y + command.value)
        elif command.action == 'S':
            return ShipStateProblem2(self.x, self.y, self.waypoint_x, self.waypoint_y - command.value)
        elif command.action == 'E':
            return ShipStateProblem2(self.x, self.y, self.waypoint_x + command.value, self.waypoint_y)
        elif command.action == 'W':
            return ShipStateProblem2(self.x, self.y, self.waypoint_x - command.value, self.waypoint_y)
        elif command.action == 'L':
            new_orientation_rads = (self.orientation + command.value) * 2 * math.pi / 360
            return ShipStateProblem2(
                self.x, self.y,
                round(math.cos(new_orientation_rads) * self.waypoint_distance),
                round(math.sin(new_orientation_rads) * self.waypoint_distance)
            )
        elif command.action == 'R':
            new_orientation_rads = (self.orientation - command.value) * 2 * math.pi / 360
            return ShipStateProblem2(
                self.x, self.y,
                round(math.cos(new_orientation_rads) * self.waypoint_distance),
                round(math.sin(new_orientation_rads) * self.waypoint_distance)
            )
        elif command.action == 'F':
            return ShipStateProblem2(
                self.x + self.waypoint_x * command.value,
                self.y + self.waypoint_y * command.value,
                self.waypoint_x,
                self.waypoint_y
            )
        else:
            raise ValueError(f'Unknown action: {command.action}')


def parse_commands(text: str) -> List[Command]:
    return [
        Command(line[0], int(line[1:]))
        for line in text.splitlines(False)
    ]


if __name__ == '__main__':
    main()
