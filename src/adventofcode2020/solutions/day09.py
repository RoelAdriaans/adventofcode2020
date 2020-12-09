from itertools import combinations
from typing import List

from adventofcode2020.utils.abstract import FileReaderSolution


class Day09:
    def check_preamble(self, integers: List[int], next_number: int) -> bool:
        for x, y in combinations(integers, r=2):
            if x + y == next_number:
                return True

        return False

    def find_first_invalid_number(self, integers: List[int]) -> int:
        for i in range(0, len(integers)):
            begin = i
            end = i + 25
            check_digit = integers[i + 25]
            preamble = integers[begin:end]
            is_valid = self.check_preamble(preamble, next_number=check_digit)
            if not is_valid:
                return check_digit
        return -1


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        integers = [int(x.strip()) for x in input_data.splitlines()]
        return self.find_first_invalid_number(integers)


class Day09PartB(Day09, FileReaderSolution):
    def find_slice(self, integers: List[int], num_to_find: int) -> int:
        for top in range(0, len(integers)):
            for bottom in range(top, len(integers)):
                total = sum(integers[top:bottom])
                if total == num_to_find:

                    # Add the largest and smallest number
                    cont_range = integers[top:bottom]
                    return max(cont_range) + min(cont_range)

                if total > num_to_find:
                    break
        return -1

    def solve(self, input_data: str) -> int:
        integers = [int(x.strip()) for x in input_data.splitlines()]

        # First we have the find the first invalid number, again
        invalid = self.find_first_invalid_number(integers)

        # And now, we have to find the a slice that adds up to those numbers
        return self.find_slice(integers, invalid)
