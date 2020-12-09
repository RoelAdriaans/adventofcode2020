from typing import List

from adventofcode2020.solutions.handheld import HandHeld
from adventofcode2020.utils.abstract import FileReaderSolution


class Day08:
    hh: HandHeld

    def run_handheld(self, instructions: List[str]) -> int:
        self.hh = HandHeld()
        self.hh.load_instructions(instructions)
        return self.hh.run(infite_loop_detection=True)


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run_handheld(input_data.splitlines())


class Day08PartB(Day08, FileReaderSolution):
    def run_until_finished_handheld(self, instructions: List[str]) -> int:
        self.hh = HandHeld()
        self.hh.load_instructions(instructions)
        return self.hh.run_until_finished_return_acc(infite_loop_detection=True)

    def solve(self, input_data: str) -> int:
        instructions = input_data.splitlines()

        for location_to_change in range(len(instructions)):
            # Create a copy from the instructions and change that
            changed_instr = instructions[:]

            if "jmp" in changed_instr[location_to_change]:
                changed_instr[location_to_change] = changed_instr[
                    location_to_change
                ].replace("jmp", "nop")

            elif "nop" in changed_instr[location_to_change]:
                changed_instr[location_to_change] = changed_instr[
                    location_to_change
                ].replace("nop", "jmp")

            else:
                # We only change nop and jmp instructions
                continue

            # Run the program. If the program returns a value, we are done, else we
            # continue
            res = self.run_until_finished_handheld(changed_instr)
            if res:
                return res
        return -1
