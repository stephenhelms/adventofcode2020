from problem import compute_solution, find_magic_timestamp, find_next_bus_and_wait_time, parse_notes

NOTES = """\
939
7,13,x,x,59,x,31,19\
"""


def test_day13_find_next_bus_and_timestamp():
    earliest_deparature, bus_schedules = parse_notes(NOTES)
    bus, wait_time = find_next_bus_and_wait_time(earliest_deparature, bus_schedules)
    assert bus == 59
    assert wait_time == 5


def test_day13_compute_solution():
    assert compute_solution(59, 5) == 295


def test_day13_find_magic_timestamp():
    earliest_deparature, bus_schedules = parse_notes(NOTES)
    assert find_magic_timestamp(bus_schedules) == 1068781
