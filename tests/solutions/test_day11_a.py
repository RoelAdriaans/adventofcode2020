import pytest

from adventofcode2020.solutions.day11 import Day11PartA


class TestDay11PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""",
                37,
            )
        ],
    )
    def test_day11a_solve(self, input_data, expected_result):
        solution = Day11PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day11a_data(self):
        """ Result we got when we did the real solution """
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res != 6415  # Too high
        assert res == 2281
