from problem import count_trees_hit, multiply_trees_hit_on_angles, parse_landscape

LANDSCAPE = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#\
"""


def test_day3_solve_problem1():
    assert count_trees_hit(parse_landscape(LANDSCAPE), 3, 1) == 7


def test_da3_solve_problem2():
    assert multiply_trees_hit_on_angles(parse_landscape(LANDSCAPE), [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]) == 336


def test_day3_parse_landscape():
    parsed = parse_landscape(LANDSCAPE)
    assert len(parsed) == 11
    assert not any('\n' in row for row in parsed)
