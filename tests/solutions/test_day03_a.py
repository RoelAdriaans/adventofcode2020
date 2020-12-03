import pytest

from adventofcode2020.solutions.day03 import Day03PartA


class TestDay03PartA:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day03a_solve(self, input_data, expected_result):
        solution = Day03PartA()
        result = solution.solve(input_data)
        assert result == expected_result


    def test_day03a_data(self):
        """ Result we got when we did the real solution """
        solution = Day03PartA()
        res = solution("day_03/day03.txt")
        assert res != 105
        assert res == 0
