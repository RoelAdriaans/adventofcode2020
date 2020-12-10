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
        differences: typing.Counter[int] = Counter()

        # Take the lowest

        while joltages:
            top = joltages.popleft()
            diff = top - min_joltage
            differences[diff] += 1

            min_joltage = top

        return differences

    def find_combinations(self, joltages: List[int]) -> int:

        connections = {joltages[-1]: 1}

        for adapter in reversed(joltages[:-1]):
            connections[adapter] = sum(
                connections.get(adapter + i, 0) for i in range(1, 4)
            )
        return connections[0]


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
        joltages = sorted(int(j.strip()) for j in input_data.splitlines())

        joltages.insert(0, 0)

        comb = self.find_combinations(joltages)

        return comb
