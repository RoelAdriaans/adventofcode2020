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

    def __repr__(self) -> str:
        if self.vert > 0:
            vert = "North"
        else:
            vert = "South"

        if self.horiz > 0:
            horiz = "East"
        else:
            horiz = "West"

        return f"{abs(self.horiz)} {horiz}, {abs(self.vert)} {vert}"


@dataclass
class Waypoint:
    location: Location

    def __init__(self):
        # Set starting location to 10 West, 1 north
        self.location = Location(horiz=10, vert=1)
        self.quadrant = Direction.NORTH

    def move(self, delta_vert, delta_horiz) -> Location:
        self.location = Location(
            vert=self.location.vert + delta_vert,
            horiz=self.location.horiz + delta_horiz,
        )

        return self.location


@dataclass
class Ship:
    direction: Direction
    location: Location

    def __init__(self, direction: Direction):
        self.direction = direction
        # Set starting location to 0,-
        self.location = Location(0, 0)

    def move(self, delta_vert, delta_horiz) -> Location:
        self.location = Location(
            vert=self.location.vert + delta_vert,
            horiz=self.location.horiz + delta_horiz,
        )

        return self.location


class Day12:
    ship: Ship
    waypoint: Waypoint

    def compute_manhathan(self) -> int:
        return abs(self.ship.location.vert) + abs(self.ship.location.horiz)


class Day12PartA(Day12, FileReaderSolution):
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

    def solve(self, input_data: str) -> int:

        instructions = [
            Instruction.from_str(input_str.strip())
            for input_str in input_data.splitlines()
        ]

        self.ship = Ship(direction=Direction.EAST)

        self.parse_instructions(instructions)

        return self.compute_manhathan()


class Day12PartB(Day12, FileReaderSolution):
    def parse_instructions(self, instructions: List[Instruction]):
        for inst in instructions:
            action = inst.action.value
            if action == "F":
                # Move the ship forward x number of units
                # (Vert, Horizontal) movement
                # Action F means to move forward to the waypoint a number of
                # times equal to the given value.
                delta_vert = self.waypoint.location.vert * inst.value
                deltra_horiz = self.waypoint.location.horiz * inst.value
                self.ship.move(delta_vert=delta_vert, delta_horiz=deltra_horiz)

            elif action == "R" or action == "L":
                # Turn the waypoint around, left or right
                # We have the values 90, 180 or 270 degrees turning
                steps = inst.value // 90 % 4

                for _ in range(steps):
                    horiz = self.waypoint.location.horiz
                    vert = self.waypoint.location.vert
                    # If we turn left, we go backwards
                    if action == "L":
                        direction = -1
                    else:
                        direction = 1

                    if horiz <= 0 and vert > 0:
                        quadrant = Direction.WEST
                    elif horiz < 0 and vert <= 0:
                        quadrant = Direction.SOUTH
                    elif horiz > 0 and vert <= 0:
                        quadrant = Direction.EAST
                    elif horiz >= 0 and vert > 0:
                        quadrant = Direction.NORTH
                    else:
                        raise ValueError(
                            f"Unknown quadrant for {vert=} {horiz=} "
                            f"{self.waypoint.location=}"
                        )

                    new_quadrant = Direction.get_next(quadrant, direction)
                    # Horiz, Vert
                    directions = {
                        Direction.NORTH: (abs(horiz), abs(vert)),  # Horiz
                        Direction.EAST: (abs(horiz), abs(vert) * -1),  # Vertical
                        Direction.SOUTH: (abs(horiz) * -1, abs(vert) * -1),  # Horiz
                        Direction.WEST: (abs(horiz) * -1, abs(vert)),  # Vert
                    }

                    new_horiz, new_vert = directions[new_quadrant]
                    new_location = Location(horiz=new_horiz, vert=new_vert)
                    self.waypoint.location = new_location

            elif action == "N":
                self.waypoint.move(delta_vert=inst.value, delta_horiz=0)
            elif action == "S":
                self.waypoint.move(delta_vert=(-1 * inst.value), delta_horiz=0)
            elif action == "E":
                self.waypoint.move(delta_vert=0, delta_horiz=inst.value)
            elif action == "W":
                self.waypoint.move(delta_vert=0, delta_horiz=(-1 * inst.value))
            else:
                raise ValueError(f"Unknown action {action}")

    def solve(self, input_data: str) -> int:
        instructions = [
            Instruction.from_str(input_str.strip())
            for input_str in input_data.splitlines()
        ]

        self.ship = Ship(direction=Direction.EAST)
        self.waypoint = Waypoint()

        self.parse_instructions(instructions)

        return self.compute_manhathan()
