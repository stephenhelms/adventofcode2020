import itertools as it
from pathlib import Path
from typing import Iterable, Set, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    state_3d = parse_initial_state(DATASET.read_text(), 3)
    for _ in range(6):
        state_3d = compute_next_state(state_3d)
    print('Problem 1: ', len(state_3d))

    state_4d = parse_initial_state(DATASET.read_text(), 4)
    for _ in range(6):
        state_4d = compute_next_state(state_4d)
    print('Problem 1: ', len(state_4d))


def parse_initial_state(text: str, n_dim: int = 3) -> Set[Tuple]:
    other_dims = [0] * (n_dim - 2)
    return {
        (x, y, *other_dims)
        for x, line in enumerate(text.splitlines(False))
        for y, char in enumerate(line)
        if char == '#'
    }


def compute_next_state(active_cubes: Set[Tuple[int, int, int]]):
    all_neighbors: Set[Tuple] = set()
    next_state: Set[Tuple] = set()
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


def iter_adjacent_cubes(cube: Tuple) -> Iterable[Tuple]:
    dim_iterators = (range(cube[dim_idx] - 1, cube[dim_idx] + 2) for dim_idx in range(len(cube)))
    for neighbor in it.product(*dim_iterators):
        if neighbor == cube:
            continue
        else:
            yield neighbor


if __name__ == '__main__':
    main()
