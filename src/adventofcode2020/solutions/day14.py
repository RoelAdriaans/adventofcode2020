import re
import typing
from collections import defaultdict
from dataclasses import dataclass
from typing import List

from adventofcode2020.utils.abstract import FileReaderSolution


@dataclass
class Instruction:
    address: int
    value: int


@dataclass
class Program:
    bitmask: str
    entries: List[Instruction]


class Day14:
    memory = typing.DefaultDict[int, int]

    @staticmethod
    def parse_programs(input_data: str) -> List[Program]:
        parts = input_data.split("mask")
        programs = []
        for part in parts:
            if not part:
                continue

            lines = part.splitlines()
            mask = lines[0].replace("=", "").strip()

            entries = []
            for line in lines[1:]:
                matches = re.match(r"mem\[(\d*)\] = (\d*)", line)
                # entries[int(matches[1])] = int(matches[2])
                entries.append(
                    Instruction(address=int(matches[1]), value=int(matches[2]))
                )

            prog = Program(bitmask=mask, entries=entries)
            programs.append(prog)
        return programs

    def process_programs(self, programs: List[Program]):
        """
        Process the instructions in the `programs` list
        mask:
        x - Don't case
        1 - Leave at 1
        0 - Leave at 0
        """
        for prog in programs:
            bits_zero = int(prog.bitmask.replace("X", "1"), 2)
            bits_one = int(prog.bitmask.replace("X", "0"), 2)

            for instr in prog.entries:
                value = instr.value
                # Bitwise mask zero to zero, keeping X as 1
                value &= bits_zero
                # Bitwise OR, keeping X as 0
                value |= bits_one

                self.memory[instr.address] = value

    def compute_sum(self) -> int:
        return sum(self.memory.values())


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.memory = defaultdict(int)

        programs = self.parse_programs(input_data)
        self.process_programs(programs)
        return self.compute_sum()


class Day14PartB(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
