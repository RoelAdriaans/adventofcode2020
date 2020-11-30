import pytest

from adventofcode2020.solutions.day01 import Day01PartA


class TestDay01PartA:
    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day01a_solve(self, input_data, expected_result):
        solution = Day01PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day01a_data(self):
        """ Result we got when we did the real solution """
        solution = Day01PartA()
        res = solution("day_01/day01.txt")
        assert res == 0
