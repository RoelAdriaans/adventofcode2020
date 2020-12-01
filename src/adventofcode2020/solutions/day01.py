import math
from itertools import combinations

from adventofcode2020.utils.abstract import FileReaderSolution


class Day01:
    @staticmethod
    def compute_factor(input_data, n):
        ints = [int(x) for x in input_data.split("\n")]
        for x in combinations(ints, n):
            if sum(x) == 2020:
                return math.prod(x)
        return -1


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.compute_factor(input_data, 2)


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.compute_factor(input_data, 3)
