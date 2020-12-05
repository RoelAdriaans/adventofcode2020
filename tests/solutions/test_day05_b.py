import pytest

from adventofcode2020.solutions.day05 import Day05PartB


class TestDay05PartB:
    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day05b_solve(self, input_data, expected_result):
        solution = Day05PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day05b_data(self):
        """ Result we got when we did the real solution """
        solution = Day05PartB()
        res = solution("day_05/day05.txt")
        assert res == 0
