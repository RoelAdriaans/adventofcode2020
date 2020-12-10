import pytest

from adventofcode2020.solutions.day10 import Day10PartA


class TestDay10PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                """16
10
15
5
1
11
7
19
6
12
4""",
                35,
            ),
        ],
    )
    def test_day10a_solve(self, input_data, expected_result):
        solution = Day10PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day10a_data(self):
        """ Result we got when we did the real solution """
        solution = Day10PartA()
        res = solution("day_10/day10.txt")
        assert res == 1700
