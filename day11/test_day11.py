from problem import count_occupied_adjacent_seats, count_occupied_seats, encode_layout, parse_layout, simulate_seating

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


def test_day11_count_adjacent_occupied_seats():
    layout = parse_layout(LAYOUT_STEPS[1])
    assert count_occupied_adjacent_seats(layout, 0, 2) == 4


def test_day11_simulate_seating():
    prev_layout = parse_layout(LAYOUT_STEPS[0])
    for round, expected_layout_text in enumerate(LAYOUT_STEPS[1:]):
        print(f'round {round + 1}...')
        expected_layout = parse_layout(expected_layout_text)
        output = simulate_seating(prev_layout)
        print(encode_layout(output))
        assert output == expected_layout
        prev_layout = expected_layout
    assert simulate_seating(prev_layout) == prev_layout


def test_day11_count_occupied_seats():
    final_layout = parse_layout(LAYOUT_STEPS[-1])
    assert count_occupied_seats(final_layout) == 37
