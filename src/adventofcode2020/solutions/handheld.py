from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Set

logger = logging.getLogger(__name__)


class ProgramFinished(Exception):
    """
    This exception is raised when the program is finished.
    This exception is usually not a fatal error, but used for control structure.
    """

    pass


class Opcode(Enum):
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"


@dataclass
class Instruction:
    opcode: Opcode
    argument: int


class HandHeld:
    """
    My first handheld computer!
    Brand: Snoby (Totally not related to Sony)
    """

    accumulator: int
    program_counter: int
    instructions: Dict[int, Instruction]
    pc_seen: Set

    def __init__(self):
        self.reset()

    def reset(self):
        self.accumulator = 0
        self.program_counter = 0
        self.pc_seen = set()

    def load_instructions(self, instructions: List[str]):
        self.accumulator = 0
        self.instructions = {}

        for i, instruction_line in enumerate(instructions):
            opcode, argument = instruction_line.split(" ")
            instr = Instruction(opcode=Opcode(opcode), argument=int(argument))
            self.instructions[i] = instr

    def process_instruction(self, infite_loop_detection=False) -> Any:
        logger.debug(
            f"Processing instruction - {self.accumulator=} - "
            f"Instruction: {self.instructions[self.program_counter]}"
            f"{self.program_counter=}"
        )

        op = self.instructions[self.program_counter].opcode
        arg = self.instructions[self.program_counter].argument

        if not op:
            # This instruction might not be needed
            raise ProgramFinished

        if infite_loop_detection and self.program_counter in self.pc_seen:
            # Another option here it to raise van InfiteLoopException with the
            # accumulator value as argument?
            # This will make returns in the future for other programs easier..
            return self.accumulator

        elif infite_loop_detection:
            self.pc_seen.add(self.program_counter)

        if op == Opcode.ACC:
            # acc increases or decreases a single global value called the accumulator
            # by the value given in the argument
            self.accumulator += arg
            self.program_counter += 1

        elif op == Opcode.JMP:
            # jmp jumps to a new instruction relative to itself.
            self.program_counter += arg

        elif op == Opcode.NOP:
            # stands for No OPeration - it does nothing.
            self.program_counter += 1

        else:
            raise ValueError(f"Unknown opcode: {op}")

        if self.program_counter >= len(self.instructions):
            # We are done
            raise ProgramFinished

    def run(self, infite_loop_detection: bool = True) -> int:
        """
        Run the Handheld computer.

        When `infite_loop_detection` is enabled, the computer will return as soon
        as instructions are repeated. The current value in the `accumulator` is
        returned.
        """
        res = 0
        try:
            while True:
                res = self.process_instruction(infite_loop_detection)
                if res not in (0, None):
                    return res
        except ProgramFinished:
            return res

    def run_return_or_raise(self, infite_loop_detection: bool) -> int:
        while True:
            res = self.process_instruction(infite_loop_detection)
            if res is not None:
                return res

    def run_until_finished_return_acc(self, infite_loop_detection: bool) -> int:
        """
        Return until we are finished and return the value in the accumulator
        """
        while True:
            try:
                res = self.process_instruction(infite_loop_detection)
                if res is not None:
                    # We are returning from an infinite loop, but we only care
                    # for the value when we reach the end of the program
                    return False
            except ProgramFinished:
                return self.accumulator
