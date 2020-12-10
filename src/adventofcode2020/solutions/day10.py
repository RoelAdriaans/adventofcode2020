import typing
from collections import Counter, deque
from typing import List

from adventofcode2020.utils.abstract import FileReaderSolution


class Day10:
    def find_diferences(self, joltages: deque) -> typing.Counter:
        # Offset higher is +3
        max_joltage = max(joltages) + 3

        joltages.append(max_joltage)
        min_joltage = 0
        differences = Counter()

        # Take the lowest

        while joltages:
            top = joltages.popleft()
            diff = top - min_joltage
            differences[diff] += 1

            min_joltage = top

        return differences


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        joltages = sorted(int(j.strip()) for j in input_data.splitlines())

        # Dequee is pronounced as `deck`
        dck = deque(joltages)
        differences = self.find_diferences(dck)

        one = differences[1]
        three = differences[3]
        return one * three


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
