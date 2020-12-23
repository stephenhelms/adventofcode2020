from enum import Enum
from pathlib import Path
from typing import Callable, Iterable, List

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    for problem, count_method, max_tolerated_occupied_seats in (
        (1, count_occupied_adjacent_seats, 4),
        (2, count_occupied_visible_seats, 5),
    ):
        current_layout = parse_layout(DATASET.read_text())
        rounds = 0
        while True:
            rounds += 1
            next_layout = simulate_seating(current_layout, count_method, max_tolerated_occupied_seats)
            if encode_layout(current_layout) == encode_layout(next_layout):
                break
            current_layout = next_layout
        print(f'Converged after {rounds} rounds')
        print(f'Problem {problem}: ', count_occupied_seats(current_layout))


class State(Enum):
    floor = '.'
    empty = 'L'
    occupied = '#'

    def __repr__(self):
        return self.value


def parse_layout(text: str) -> List[List[State]]:
    return [[State(seat) for seat in row]
            for row in text.splitlines(False)]


def encode_layout(layout: List[List[State]]) -> str:
    return '\n'.join(''.join(seat.value for seat in row) for row in layout)


def simulate_seating(layout: List[List[State]],
                     count_method: Callable[[List[List[State]], int, int], int],
                     max_tolerated_occupied_seats: int = 4) -> List[List[State]]:
    num_rows = len(layout)
    num_cols = len(layout[0])
    return [
        [
            update_seat_state(layout, row_idx, col_idx, count_method,
                              max_tolerated_occupied_seats=max_tolerated_occupied_seats)
            for col_idx in range(num_cols)
        ] for row_idx in range(num_rows)
    ]


def update_seat_state(layout: List[List[State]], row_idx: int, col_idx: int,
                      count_method: Callable[[List[List[State]], int, int], int],
                      max_tolerated_occupied_seats: int = 4) -> State:
    current_state = layout[row_idx][col_idx]
    if current_state == State.floor:
        return State.floor

    num_occupied_adajcent = count_method(layout, row_idx, col_idx)
    if current_state == State.empty and num_occupied_adajcent == 0:
        return State.occupied
    elif current_state == State.occupied and num_occupied_adajcent >= max_tolerated_occupied_seats:
        return State.empty
    else:
        return current_state


def count_occupied_adjacent_seats(layout: List[List[State]], row_idx: int, col_idx: int) -> int:
    return sum(1 for adjacent_seat in iter_adjacent_seats(layout, row_idx, col_idx)
               if adjacent_seat == State.occupied)


def iter_adjacent_seats(layout: List[List[State]], row_idx: int, col_idx: int) -> Iterable[State]:
    num_rows = len(layout)
    num_cols = len(layout[0])
    for row_delta in (-1, 0, 1):
        adjacent_row_idx = row_idx + row_delta
        for col_delta in (-1, 0, 1):
            adjacent_col_idx = col_idx + col_delta
            if (
                    0 <= adjacent_row_idx < num_rows and
                    0 <= adjacent_col_idx < num_cols and
                    not (row_delta == 0 and col_delta == 0)
            ):
                yield layout[adjacent_row_idx][adjacent_col_idx]


def count_occupied_visible_seats(layout: List[List[State]], row_idx: int, col_idx: int) -> int:
    return sum(1 for adjacent_seat in iter_visible_seats(layout, row_idx, col_idx)
               if adjacent_seat == State.occupied)


def iter_visible_seats(layout: List[List[State]], row_idx: int, col_idx: int) -> Iterable[State]:
    # the iter_adjacent_seats could be considered a special case of this one with max_steps = 1
    num_rows = len(layout)
    num_cols = len(layout[0])
    for row_delta in (-1, 0, 1):
        for col_delta in (-1, 0, 1):
            if row_delta == 0 and col_delta == 0:
                continue
            steps = 1
            while True:
                visible_row_idx = row_idx + steps*row_delta
                visible_col_idx = col_idx + steps*col_delta
                if not (0 <= visible_row_idx < num_rows and 0 <= visible_col_idx < num_cols):
                    break
                state = layout[visible_row_idx][visible_col_idx]
                if state != State.floor:
                    yield state
                    break
                else:
                    steps += 1


def count_occupied_seats(layout: List[List[State]]) -> int:
    return sum(seat == State.occupied
               for row in layout
               for seat in row)


if __name__ == '__main__':
    main()
