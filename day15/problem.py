import itertools as it
from typing import Iterable, Tuple


def main():
    starting_seq = 14, 8, 16, 0, 1, 17
    print('Problem 1: ', compute_nth_number(starting_seq, 2020))
    print('Problem 2: ', compute_nth_number(starting_seq, 30000000))


def compute_nth_number(starting_seq: Tuple[int], pos: int) -> int:
    return next(it.islice(iter_spoken_numbers(starting_seq),
                          pos - len(starting_seq) - 1,
                          pos - len(starting_seq)))


def iter_spoken_numbers(starting_seq: Tuple[int]) -> Iterable[int]:
    number_round = {
        number: (round_idx, round_idx)
        for number, round_idx
        in zip(starting_seq, range(len(starting_seq)))
    }
    last_spoken = starting_seq[-1]
    round_idx = len(starting_seq)
    while True:
        state = number_round.get(last_spoken, (round_idx, round_idx))
        rounds_since_prev_spoken = state[1] - state[0]
        yield rounds_since_prev_spoken
        last_spoken = rounds_since_prev_spoken
        number_round[last_spoken] = (number_round.get(last_spoken, (round_idx, round_idx))[1], round_idx)
        round_idx += 1


if __name__ == '__main__':
    main()
