from typing import List

from adventofcode2020.solutions.handheld import HandHeld, ProgramFinished
from adventofcode2020.utils.abstract import FileReaderSolution


class Day08:
    hh: HandHeld

    def run_handheld(self, instructions: List[str]) -> int:
        self.hh = HandHeld()
        self.hh.load_instructions(instructions)
        try:
            return self.hh.run(infite_loop_detection=True)
        except ProgramFinished:
            return True


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run_handheld(input_data.splitlines())


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
