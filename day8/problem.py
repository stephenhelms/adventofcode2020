from pathlib import Path
from typing import Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    program = Program(DATASET.read_text())
    print('Problem 1: ', program.run())
    print('Problem 2: ', find_final_acc_value_finite_program(program))


class InfiniteLoopError(Exception):
    pass


class Program:
    def __init__(self, code: str):
        self.steps = [self.parse_step(step) for step in code.splitlines(False)]
        self.acc = 0
        self.visited = set()

    @staticmethod
    def parse_step(step: str) -> Tuple[str, int]:
        command, amount = step.split(' ')
        return command, int(amount)

    def run(self, raise_on_infinite_loop: bool = False):
        self.acc = 0
        self.visited.clear()
        idx = 0
        while idx < len(self.steps):
            command, amount = self.steps[idx]
            idx = self.run_command(command, amount, idx)
            if idx in self.visited:
                if raise_on_infinite_loop:
                    raise InfiniteLoopError()
                else:
                    break
            else:
                self.visited.add(idx)
        return self.acc

    def run_command(self, command: str, amount: int, idx: int):
        if command == 'acc':
            self.acc += amount
            idx += 1
        elif command == 'jmp':
            idx += amount
        elif command == 'nop':
            idx += 1
        else:
            raise ValueError(f'Unknown command: {command}')
        return idx


def find_final_acc_value_finite_program(program: Program) -> int:
    for idx, (command, amount) in enumerate(program.steps):
        if command == 'acc':
            continue
        program.steps[idx] = ('jmp' if command == 'nop' else 'nop', amount)
        try:
            return program.run(raise_on_infinite_loop=True)
        except InfiniteLoopError:
            program.steps[idx] = (command, amount)
    raise RuntimeError('No solution found.')


if __name__ == '__main__':
    main()
