from collections import defaultdict, deque
from typing import Dict

from adventofcode2020.utils.abstract import FileReaderSolution


class Day11:
    def str_to_map(self, input_data) -> Dict[int, Dict]:
        grid = {}
        for row, line in enumerate(input_data.splitlines()):
            grid[row] = {k: v for k, v in enumerate(line)}

        return grid

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

    def generation(self, grid) -> Dict[int, Dict]:
        # First we will compute the numbers, and then assign it to a new dict
        # This works, but it not really performance proof..

        new_grid = defaultdict(dict)
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == ".":
                    new_grid[row][col] = "."
                    continue

                count = self.count_next_to_it(grid, row, col)
                if count == 0:
                    new_grid[row][col] = "#"

                elif grid[row][col] == "#" and count >= 4:
                    # If a seat is occupied (#) and four or more seats adjacent to it
                    # are also occupied, the seat becomes empty
                    new_grid[row][col] = "L"

                elif grid[row][col] == "#" and count < 4:
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
        print("\n")
        for row, value in grid.items():
            print("".join(value.values()))
        print("\n")


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        # Keep a sliding average
        average = deque()

        map = self.str_to_map(input_data)
        filled = self.count_filled(map)

        while True:
            map = self.generation(map)
            # Filled seats
            filled = self.count_filled(map)
            average.append(filled)

            if len(average) >= 5:
                popped = average.popleft()
                if popped == filled:
                    return filled

        return -1


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
