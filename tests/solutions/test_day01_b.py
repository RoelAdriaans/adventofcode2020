import pytest

from adventofcode2020.solutions.day01 import Day01PartB


class TestDay01PartB:
    def test_day01b_data(self):
        """ Result we got when we did the real solution """
        solution = Day01PartB()
        res = solution("day_01/day01.txt")
        assert res == 0
