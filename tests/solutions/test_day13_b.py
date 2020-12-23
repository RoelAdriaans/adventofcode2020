import pytest

from adventofcode2020.solutions.day13 import Day13PartB


class TestDay13PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("0\n17,x,13,19", 3417),
            ("939\n7,13,x,x,59,x,31,19", 1068781),
        ],
    )
    def test_day13b_solve(self, input_data, expected_result):
        solution = Day13PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day13b_data(self):
        """ Result we got when we did the real solution """
        solution = Day13PartB()
        res = solution("day_13/day13.txt")
        assert res == 266204454441577
