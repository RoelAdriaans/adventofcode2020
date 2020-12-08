import pytest

from adventofcode2020.solutions.day06 import Day06PartA


class TestDay06PartA:
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
                11,
            )
        ],
    )
    def test_day06a_solve(self, input_data, expected_result):
        solution = Day06PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day06a_data(self):
        """ Result we got when we did the real solution """
        solution = Day06PartA()
        res = solution("day_06/day06.txt")
        assert res == 6549
