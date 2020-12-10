import pytest

from adventofcode2020.solutions.day10 import Day10PartB


class TestDay10PartB:
    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day10b_solve(self, input_data, expected_result):
        solution = Day10PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day10b_data(self):
        """ Result we got when we did the real solution """
        solution = Day10PartB()
        res = solution("day_10/day10.txt")
        assert res == 0
