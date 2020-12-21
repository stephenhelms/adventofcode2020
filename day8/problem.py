from pathlib import Path
from typing import Dict, Tuple

DATASET = Path(__file__).parent / 'dataset.txt'


def main():
    program = Program(DATASET.read_text())
    print('Problem 1: ', program.run())


class Program:
    def __init__(self, code: str):
        self.steps = [self.parse_step(step) for step in code.splitlines(False)]
        self.acc = 0
        self.visited = set()

    @staticmethod
    def parse_step(step: str) -> Tuple[str, int]:
        command, amount = step.split(' ')
        return command, int(amount)

    def run(self):
        idx = 0
        while True:
            command, amount = self.steps[idx]
            idx = self.run_command(command, amount, idx)
            if idx in self.visited:
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

        if idx >= len(self.steps):
            idx -= len(self.steps)
        return idx


if __name__ == '__main__':
    main()
