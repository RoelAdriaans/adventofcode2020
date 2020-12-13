from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, NamedTuple

from adventofcode2020.utils.abstract import FileReaderSolution


class Instruction(NamedTuple):
    action: Direction
    value: int

    @staticmethod
    def from_str(input_str: str) -> Instruction:
        return Instruction(action=Direction(input_str[0]), value=int(input_str[1:]))


class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"
    RIGHT = "R"
    LEFT = "L"
    FORWARD = "F"

    @staticmethod
    def get_next(direction: Direction, n: int) -> Direction:
        directions = (Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST)

        # Current location:
        idx = directions.index(direction)
        new_idx = (idx + n) % 4
        return directions[new_idx]


class Location(NamedTuple):
    vert: int = 0
    horiz: int = 0


@dataclass
class Ship:
    direction: Direction
    location: Location

    visitied_locations: List[Location]

    def __init__(self, direction: Direction):
        self.direction = direction
        # Set starting location to 0,-
        self.location = Location(0, 0)
        self.visitied_locations = [self.location]

    def move(self, delta_vert, delta_horiz) -> Location:
        self.location = Location(
            vert=self.location.vert + delta_vert,
            horiz=self.location.horiz + delta_horiz,
        )

        self.visitied_locations.append(self.location)
        return self.location


class Day12:
    ship: Ship

    def parse_instructions(self, instructions: List[Instruction]):

        for inst in instructions:
            action = inst.action.value
            if action == "F":
                # Move the ship forward x number of units
                # (Vert, Horizontal) movement
                directions = {
                    Direction.NORTH: (inst.value, 0),
                    Direction.EAST: (0, inst.value),
                    Direction.SOUTH: (-1 * inst.value, 0),
                    Direction.WEST: (0, -1 * inst.value),
                }

                delta_vert, deltra_horiz = directions[self.ship.direction]
                self.ship.move(delta_vert=delta_vert, delta_horiz=deltra_horiz)
            elif action == "R" or action == "L":
                # Turn left or right
                # We have the values 90, 180 or 270 degrees turning
                steps = inst.value // 90 % 4

                # If we turn left, we go backwards
                if action == "L":
                    steps = steps * -1

                new_direction = Direction.get_next(self.ship.direction, steps)
                self.ship.direction = new_direction
            elif action == "N":
                self.ship.move(delta_vert=inst.value, delta_horiz=0)
            elif action == "S":
                self.ship.move(delta_vert=(-1 * inst.value), delta_horiz=0)
            elif action == "E":
                self.ship.move(delta_vert=0, delta_horiz=inst.value)
            elif action == "W":
                self.ship.move(delta_vert=0, delta_horiz=(-1 * inst.value))
            else:
                raise ValueError(f"Unknown action {action}")

    def compute_manhathan(self) -> int:
        return abs(self.ship.location.vert) + abs(self.ship.location.horiz)


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:

        instructions = [
            Instruction.from_str(input_str.strip())
            for input_str in input_data.splitlines()
        ]

        self.ship = Ship(direction=Direction.EAST)

        self.parse_instructions(instructions)
        print(f"Location is now: {self.ship.location}")
        return self.compute_manhathan()


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
