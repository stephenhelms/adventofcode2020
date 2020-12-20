from pathlib import Path
from typing import List

LANDSCAPE = Path(__file__).parent / 'dataset.txt'


def main():
    landscape = LANDSCAPE.read_text()
    print('Problem 1: ', count_trees_hit(landscape, 3, 1))


def count_trees_hit(landscape: str, num_right: int, num_down: int) -> int:
    parsed_landscape = parse_landscape(landscape)
    landscape_x_dim = len(parsed_landscape[0])
    landscape_y_dim = len(parsed_landscape)
    x, y = 0, 0
    num_trees = 0
    while y < landscape_y_dim:
        x += num_right
        if x >= landscape_x_dim:
            x -= landscape_x_dim
        y += num_down
        if y >= landscape_y_dim:
            break
        if parsed_landscape[y][x] == '#':
            num_trees += 1
    return num_trees


def parse_landscape(landscape: str) -> List[str]:
    return list(landscape.splitlines(False))


if __name__ == '__main__':
    main()
