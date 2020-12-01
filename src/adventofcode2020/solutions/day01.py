from adventofcode2020.utils.abstract import FileReaderSolution
from itertools import permutations

class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        ints = [int(x) for x in input_data.split("\n")]
        for x in permutations(ints, 2):
            if sum(x) == 2020:
                return x[0] * x[1]


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        ints = [int(x) for x in input_data.split("\n")]
        for x in permutations(ints, 3):
            if sum(x) == 2020:
                return x[0] * x[1] * x[2]
