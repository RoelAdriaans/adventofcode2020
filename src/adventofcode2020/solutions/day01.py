from adventofcode2020.utils.abstract import FileReaderSolution


class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return len(input_data)


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError