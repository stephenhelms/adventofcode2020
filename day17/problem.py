import itertools as it
from pathlib import Path
from typing import Iterable, Set, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    state = parse_initial_state(DATASET.read_text())
    for _ in range(6):
        state = compute_next_state(state)
    print('Problem 1: ', len(state))


def parse_initial_state(text: str) -> Set[Tuple[int, int, int]]:
    z = 0
    return {
        (x, y, z)
        for x, line in enumerate(text.splitlines(False))
        for y, char in enumerate(line)
        if char == '#'
    }


def compute_next_state(active_cubes: Set[Tuple[int, int, int]]):
    all_neighbors: Set[Tuple[int, int, int]] = set()
    next_state: Set[Tuple[int, int, int]] = set()
    for active_cube in active_cubes:
        adjacent = set(iter_adjacent_cubes(active_cube))
        all_neighbors |= adjacent
        num_active = sum(1 for neighbor in adjacent if neighbor in active_cubes)
        if num_active in (2, 3):
            next_state.add(active_cube)
    for inactive_cube in (all_neighbors - active_cubes):
        adjacent = iter_adjacent_cubes(inactive_cube)
        num_active = sum(1 for neighbor in adjacent if neighbor in active_cubes)
        if num_active == 3:
            next_state.add(inactive_cube)
    return next_state


def iter_adjacent_cubes(cube: Tuple[int, int, int]) -> Iterable[Tuple[int, int, int]]:
    x, y, z = cube
    for neighbor in it.product(range(x - 1, x + 2),
                               range(y - 1, y + 2),
                               range(z - 1, z + 2)):
        if neighbor == (x, y, z):
            continue
        else:
            yield neighbor


if __name__ == '__main__':
    main()
