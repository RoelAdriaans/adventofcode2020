import pytest

from adventofcode2020.solutions.day06 import Day06PartB


class TestDay06PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                """abc

a
b
c

ab
ac

a
a
a
a

b""",
                6,
            )
        ],
    )
    def test_day06b_solve(self, input_data, expected_result):
        solution = Day06PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day06b_data(self):
        """ Result we got when we did the real solution """
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 3466
