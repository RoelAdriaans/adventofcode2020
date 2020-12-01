from itertools import combinations

from adventofcode2020.utils.abstract import FileReaderSolution


class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        ints = [int(x) for x in input_data.split("\n")]
        for x in combinations(ints, 2):
            if sum(x) == 2020:
                return x[0] * x[1]
        return -1


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        ints = [int(x) for x in input_data.split("\n")]
        for x in combinations(ints, 3):
            if sum(x) == 2020:
                return x[0] * x[1] * x[2]
        return -1
