import typing
from collections import Counter

from adventofcode2020.utils.abstract import FileReaderSolution


class Day06:
    pass


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        sum = 0
        for groups in input_data.split("\n\n"):
            # Remove newlines and make it a set
            letters = set(groups.replace("\n", ""))
            sum += len(letters)
        return sum


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        sum = 0
        for groups in input_data.split("\n\n"):
            # Remove newlines and make it a set
            group_counter: typing.Counter[str] = Counter()
            for person in groups.splitlines():
                group_counter.update(person)

            # And find how many counts have len(groups.splitlines())
            length = len(groups.splitlines())
            sum += len([x for x in group_counter.values() if x == length])

        return sum
