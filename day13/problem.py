from functools import reduce
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    earliest_timestamp, bus_schedules = parse_notes(DATASET.read_text())
    next_bus, wait_time = find_next_bus_and_wait_time(earliest_timestamp, bus_schedules)
    print('Problem 1: ', compute_solution(next_bus, wait_time))
    print('Problem 2: ', find_magic_timestamp(bus_schedules))


def parse_notes(text: str) -> Tuple[int, List[Optional[int]]]:
    timestamp_line, schedule_line = text.splitlines(False)
    earliest_timestamp = int(timestamp_line)
    schedules = [int(value) if value != 'x' else None
                 for value in schedule_line.split(',')]
    return earliest_timestamp, schedules


def find_next_bus_and_wait_time(earliest_timestamp: int, schedule: List[Optional[int]]) -> Tuple[int, int]:
    ordered_bus_delays = sorted([(bus_id - earliest_timestamp % bus_id, bus_id)
                                 for bus_id in schedule if bus_id])
    wait_time, bus_id = ordered_bus_delays[0]
    return bus_id, wait_time


def compute_solution(bus: int, wait_time: int) -> int:
    return bus * wait_time


def find_magic_timestamp(schedule: List[Optional[int]]) -> int:
    constraints = list(reversed(sorted([(bus_id, offset) for offset, bus_id in enumerate(schedule) if bus_id])))
    min_possible_solution = max(bus_id - offset for bus_id, offset in constraints)
    last_solution_per_constraint = [next(iter(iter_possible_magic_solutions(bus_id, wait_time,
                                                                            min_possible_solution)))
                                    for bus_id, wait_time in constraints]
    # this is still painfully slow for the full problem but better than raw brute force,
    # there should be a more efficient solution. also code needs to be cleaned up
    while not len(set(last_solution_per_constraint)) == 1:  # no solution found
        # iterate possible solutions per constraint that are less than the next min possible solution
        # start with biggest factors and find common solution for them before iterating on smaller constraints
        for idx, (bus_id, wait_time) in enumerate(constraints):
            if last_solution_per_constraint[idx] == min_possible_solution:
                continue

            possible_solutions = iter(iter_possible_magic_solutions(bus_id, wait_time, min_possible_solution))
            while last_solution_per_constraint[idx] < min_possible_solution:
                last_solution_per_constraint[idx] = next(possible_solutions)
            min_possible_solution = max(last_solution_per_constraint)
            break
        print(last_solution_per_constraint)
    return last_solution_per_constraint[0]


def iter_possible_magic_solutions(bus_id, wait_time, earliest_possible_timestamp: int) -> Iterable[int]:
    n = earliest_possible_timestamp // bus_id
    while True:
        arrival_time = n * bus_id
        yield arrival_time - wait_time
        n += 1


if __name__ == '__main__':
    main()
