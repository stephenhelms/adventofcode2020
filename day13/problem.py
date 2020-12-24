from pathlib import Path
from typing import List, Optional, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    earliest_timestamp, bus_schedules = parse_notes(DATASET.read_text())
    next_bus, wait_time = find_next_bus_and_wait_time(earliest_timestamp, bus_schedules)
    print('Problem 1: ', compute_solution(next_bus, wait_time))


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

if __name__ == '__main__':
    main()
