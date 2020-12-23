import pytest

from adventofcode2020.solutions.day13 import Day13PartA


class TestDay13PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("939\n7,13,x,x,59,x,31,19", 295)]
    )
    def test_day13a_solve(self, input_data, expected_result):
        solution = Day13PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day13a_data(self):
        """ Result we got when we did the real solution """
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res == 2545
