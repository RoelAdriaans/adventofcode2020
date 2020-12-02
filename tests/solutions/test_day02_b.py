import pytest

from adventofcode2020.solutions.day02 import Day02PartB


class TestDay02PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc\n", 1)],
    )
    def test_day02b_solve(self, input_data, expected_result):
        solution = Day02PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day02b_data(self):
        """ Result we got when we did the real solution """
        solution = Day02PartB()
        res = solution("day_02/day02.txt")
        assert res == 294
