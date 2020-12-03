import math

from adventofcode2020.utils.abstract import FileReaderSolution


class Day03:
    def solve_options(self, input_data: str, right: int, down: int) -> int:
        count = 0
        pos = 0
        lines = input_data.split("\n")
        for idx in range(0, len(lines), down):
            line = lines[idx]
            pos_mod = pos % len(line)

            if line[pos_mod] == "#":
                count += 1

            pos += right
        return count


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.solve_options(input_data, 3, 1)


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        numbers = [
            self.solve_options(input_data, 1, 1),
            self.solve_options(input_data, 3, 1),
            self.solve_options(input_data, 5, 1),
            self.solve_options(input_data, 7, 1),
            self.solve_options(input_data, 1, 2),
        ]
        return math.prod(numbers)
