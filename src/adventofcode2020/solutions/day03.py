from adventofcode2020.utils.abstract import FileReaderSolution
import math


class Day03:
    pass


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        count = 0
        pos = 0
        lines = input_data.split("\n")
        for line in lines:
            # Going down
            pos_mod = pos % len(line)
            char_at_los = line[pos_mod]
            if char_at_los == "#":
                count += 1
            pos += 3
        return count


class Day03PartB(Day03, FileReaderSolution):
    def solve_options(self, input_data, right, down):
        count = 0
        pos = 0
        line_num = 1
        lines = input_data.split("\n")
        for line in lines:
            line_num += 1
            if down == 2 and line_num % 2:
                continue

            # Going down
            pos_mod = pos % len(line)
            char_at_los = line[pos_mod]
            if char_at_los == "#":
                count += 1
            pos += right
        return count

    def solve(self, input_data: str) -> int:
        numbers = [
            self.solve_options(input_data, 1, 1),
            self.solve_options(input_data, 3, 1),
            self.solve_options(input_data, 5, 1),
            self.solve_options(input_data, 7, 1),
            self.solve_options(input_data, 1, 2),
        ]
        return math.prod(numbers)
