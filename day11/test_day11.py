import pytest

from problem import count_occupied_adjacent_seats, count_occupied_visible_seats, count_occupied_seats, encode_layout, parse_layout, simulate_seating

LAYOUT_STEPS = [
"""\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL\
""",
"""\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##\
""",
"""\
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##\
""",
"""\
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##\
""",
"""\
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##\
""",
"""\
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##\
""",
]

LAYOUT_STEPS_PROBLEM_2 = [
"""\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL\
""",
"""\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##\
""",
"""\
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#\
""",
"""\
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#\
""",
"""\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#\
""",
"""\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#\
""",
"""\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#\
"""
]

EXAMPLE_VISIBLE_SEATS = [
(4, 3, """\
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....\
""", 8),
(1, 1, """\
.............
.L.L.#.#.#.#.
.............\
""", 0),
(3, 3, """\
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.\
""", 0),
]


def test_day11_count_adjacent_occupied_seats():
    layout = parse_layout(LAYOUT_STEPS[1])
    assert count_occupied_adjacent_seats(layout, 0, 2) == 4


@pytest.mark.parametrize('row_idx,col_idx,layout_text,num_visible', EXAMPLE_VISIBLE_SEATS)
def test_day11_count_occupied_visible_seats(row_idx, col_idx, layout_text, num_visible):
    layout = parse_layout(layout_text)
    assert count_occupied_visible_seats(layout, row_idx, col_idx) == num_visible


@pytest.mark.parametrize('layout_steps,count_method,max_tolerated_occupied_seats', [
    (LAYOUT_STEPS, count_occupied_adjacent_seats, 4),
    (LAYOUT_STEPS_PROBLEM_2, count_occupied_visible_seats, 5),
])
def test_day11_simulate_seating(layout_steps, count_method, max_tolerated_occupied_seats):
    prev_layout = parse_layout(layout_steps[0])
    for round, expected_layout_text in enumerate(layout_steps[1:]):
        print(f'round {round + 1}...')
        expected_layout = parse_layout(expected_layout_text)
        output = simulate_seating(prev_layout, count_method, max_tolerated_occupied_seats)
        print(encode_layout(output))
        assert output == expected_layout
        prev_layout = expected_layout
    assert simulate_seating(prev_layout, count_method, max_tolerated_occupied_seats) == prev_layout


def test_day11_count_occupied_seats():
    final_layout = parse_layout(LAYOUT_STEPS[-1])
    assert count_occupied_seats(final_layout) == 37
