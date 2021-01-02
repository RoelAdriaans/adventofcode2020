import re
import typing
from abc import abstractmethod
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
                matches = re.match(r"mem\[(\d*)] = (\d*)", line)
                # entries[int(matches[1])] = int(matches[2])
                entries.append(
                    Instruction(address=int(matches[1]), value=int(matches[2]))
                )

            prog = Program(bitmask=mask, entries=entries)
            programs.append(prog)
        return programs

    def compute_sum(self) -> int:
        return sum(self.memory.values())

    @abstractmethod
    def process_programs(self, programs: List[Program]):
        """ Process the program based on the version"""

    def solve(self, input_data: str) -> int:
        self.memory = defaultdict(int)

        programs = self.parse_programs(input_data)
        self.process_programs(programs)
        return self.compute_sum()


class Day14PartA(Day14, FileReaderSolution):
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


class Day14PartB(Day14, FileReaderSolution):
    @staticmethod
    def set_bit(value, bit_value, bit):
        return value | (bit_value << bit)

    @staticmethod
    def clear_bit(value, bit):
        return value & ~(1 << bit)

    @staticmethod
    def mask_to_addresses(address: int, mask: str) -> List[int]:
        """
        Convert a mask, for example
        000000000000000000000000000000X1001X
        With the address 42
        to all the applicable masks:
        000000000000000000000000000000011010  (decimal 26)
        000000000000000000000000000000011011  (decimal 27)
        000000000000000000000000000000111010  (decimal 58)
        000000000000000000000000000000111011  (decimal 59)
        """
        # First apply a mask
        bits_one = int(mask.replace("X", "0"), 2)

        # Bitwise mask zero to zero, keeping X as 1
        # Bitwise OR, keeping X as 0
        address |= bits_one

        # Apply X again:
        addresses = []
        x_positions = [35 - n for n in range(len(mask)) if mask.find("X", n) == n]

        for bits in range(pow(2, len(x_positions))):
            new_adr = address
            bit_string = f"{bits:036b}"[::-1]
            for idx, pos_index in enumerate(x_positions):
                # Convert bits integer to bits, and put every bit on the right place
                new_adr = Day14PartB.clear_bit(new_adr, pos_index)
                bit_value = int(bit_string[idx])
                new_adr = Day14PartB.set_bit(new_adr, bit_value, pos_index)

            addresses.append(new_adr)
        return addresses

    def process_programs(self, programs: List[Program]):
        """
        Process the instructions in the `programs` list
        mask. But this time, the mask is for the address line
        X - Floating, 0 or 1
        1 - Overwrite with 1
        0 - Keep as is
        """
        for prog in programs:
            for entry in prog.entries:
                addresses = self.mask_to_addresses(
                    mask=prog.bitmask, address=entry.address
                )
                for address in addresses:
                    self.memory[address] = entry.value
