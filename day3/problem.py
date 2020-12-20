from functools import reduce
from pathlib import Path
from typing import List, Tuple

LANDSCAPE = Path(__file__).parent / 'dataset.txt'


def main():
    landscape = parse_landscape(LANDSCAPE.read_text())
    print('Problem 1: ', count_trees_hit(landscape, 3, 1))
    print('Problem 2: ', multiply_trees_hit_on_angles(landscape, [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]))


def multiply_trees_hit_on_angles(landscape: List[str], angles: Tuple[int, int]) -> int:
    trees_hit = (count_trees_hit(landscape, *angle) for angle in angles)
    return reduce(lambda agg, v: agg * v, trees_hit)


def count_trees_hit(landscape: List[str], num_right: int, num_down: int) -> int:
    landscape_x_dim = len(landscape[0])
    landscape_y_dim = len(landscape)
    x, y = 0, 0
    num_trees = 0
    while y < landscape_y_dim:
        x += num_right
        if x >= landscape_x_dim:
            x -= landscape_x_dim
        y += num_down
        if y >= landscape_y_dim:
            break
        if landscape[y][x] == '#':
            num_trees += 1
    return num_trees


def parse_landscape(landscape: str) -> List[str]:
    return list(landscape.splitlines(False))


if __name__ == '__main__':
    main()
