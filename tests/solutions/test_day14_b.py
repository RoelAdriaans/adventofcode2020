import pytest

from adventofcode2020.solutions.day14 import Day14PartB


class TestDay14PartB:
    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day14b_solve(self, input_data, expected_result):
        solution = Day14PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_day14b_data(self):
        """ Result we got when we did the real solution """
        solution = Day14PartB()
        res = solution("day_14/day14.txt")
        assert res == 0
