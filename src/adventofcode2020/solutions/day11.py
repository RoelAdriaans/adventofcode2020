from abc import abstractmethod
from collections import defaultdict, deque
from typing import Deque, Dict

from adventofcode2020.utils.abstract import FileReaderSolution


class Day11:
    count_seats: int

    @abstractmethod
    def count_next_to_it(self, grid, row, col) -> int:
        """ Count the number of seats next to it/ Depends on the part"""

    def str_to_map(self, input_data) -> Dict[int, Dict]:
        grid = {}
        for row, line in enumerate(input_data.splitlines()):
            grid[row] = {k: v for k, v in enumerate(line)}

        return grid

    def generation(self, grid) -> Dict[int, Dict]:
        # First we will compute the numbers, and then assign it to a new dict
        # This works, but it not really performance proof..

        new_grid: Dict[int, Dict] = defaultdict(dict)
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == ".":
                    new_grid[row][col] = "."
                    continue

                count = self.count_next_to_it(grid, row, col)
                if count == 0:
                    new_grid[row][col] = "#"

                elif grid[row][col] == "#" and count >= self.count_seats:
                    # If a seat is occupied (#) and four or more seats adjacent to it
                    # are also occupied, the seat becomes empty
                    new_grid[row][col] = "L"

                elif grid[row][col] == "#" and count < self.count_seats:
                    # Occupied but other then 4, it stays the same
                    new_grid[row][col] = grid[row][col]

                else:
                    new_grid[row][col] = grid[row][col]

        return new_grid

    def count_filled(self, grid, char="#") -> int:
        rij = []
        for row, value in grid.items():
            rij += value.values()

        return rij.count(char)

    def print_grid(self, grid):
        from time import sleep

        sleep(0.1)
        print(chr(27) + "[2J")
        print("\n")
        for row, value in grid.items():
            print("".join(value.values()))
        print("\n")

    def run_day(self, input_data):
        average: Deque[int] = deque()

        grid = self.str_to_map(input_data)

        while True:
            grid = self.generation(grid)
            # Filled seats
            filled = self.count_filled(grid)
            average.append(filled)
            # self.print_grid(map)
            if len(average) >= 5:
                popped = average.popleft()
                if popped == filled:
                    return filled


class Day11PartA(Day11, FileReaderSolution):
    count_seats = 4

    def count_next_to_it(self, grid, row, col) -> int:
        """ Returns how many seats next to this one are filled"""
        res = [
            grid.get(row, {}).get(col - 1, 0),  # Left
            grid.get(row, {}).get(col + 1, 0),  # Right
            grid.get(row - 1, {}).get(col, 0),  # Bottom
            grid.get(row + 1, {}).get(col, 0),  # Top
            #
            grid.get(row - 1, {}).get(col - 1, 0),  # Bottom Left
            grid.get(row - 1, {}).get(col + 1, 0),  # Bottom Right
            grid.get(row + 1, {}).get(col - 1, 0),  # Top Left
            grid.get(row + 1, {}).get(col + 1, 0),  # Top Right
        ]
        return res.count("#")

    def solve(self, input_data: str) -> int:
        return self.run_day(input_data)


class Day11PartB(Day11, FileReaderSolution):
    count_seats = 5

    def find_recursive(self, grid, row, col, drow, dcol, offset=1) -> bool:
        """
        Find if a spot is taken.
        If a spot is the floor, it will look further.
        If the seat is taken, it will return True, else it will return False
        """
        spot = grid.get(row + (drow * offset), {}).get(col + (dcol * offset), None)
        if spot == ".":
            return self.find_recursive(grid, row, col, drow, dcol, offset + 1)
        elif spot == "#":
            return True
        elif spot == "L":
            return False
        elif spot is None:
            # Off the grid
            return False
        else:
            raise ValueError(f"Unknown char at {spot}")

    def count_next_to_it(self, grid, row, col) -> int:
        """
        Returns how many seats next to it are empty, but when a a seat
        is next to the floor, we look ahead!
        """
        res = [
            self.find_recursive(grid, row, col, drow, dcol)
            for drow, dcol in (
                (0, -1),  # Left
                (0, +1),  # Right
                (-1, 0),  # Top
                (+1, 0),  # Bottom
                (-1, -1),  # Bottom left
                (-1, +1),  # Bottom right
                (+1, -1),  # Top left
                (+1, +1),  # Top right
            )
        ]
        return sum(res)

    def solve(self, input_data: str) -> int:
        return self.run_day(input_data)
