import pytest

from adventofcode2020.solutions.day11 import Day11PartB


class TestDay11PartB:
    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day11b_solve(self, input_data, expected_result):
        solution = Day11PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day11b_data(self):
        """ Result we got when we did the real solution """
        solution = Day11PartB()
        res = solution("day_11/day11.txt")
        assert res == 0
