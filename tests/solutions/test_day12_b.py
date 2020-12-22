import pytest

from adventofcode2020.solutions.day12 import Day12PartB


class TestDay12PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (["F10", "N3", "F7", "R90", "F11"], 286),
            (
                [
                    "F10",
                    "R180",
                    "F20",
                    "L180",
                    "F20",
                    "R90",
                    "R90",
                    "F20",
                    "L90",
                    "L90",
                    "F10",
                ],
                0,
            ),
        ],
    )
    def test_day12b_solve(self, input_data, expected_result):
        input_str = "\n".join(input_data)
        solution = Day12PartB()
        result = solution.solve(input_str)
        assert result == expected_result

    def test_day12b_data(self):
        """ Result we got when we did the real solution """
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res < 35575  # Too high
        assert res < 58937  # Too High
        assert res != 18369
        assert res != 263381
        assert res != 26775
        assert res != 30045
        assert res != 77469
        assert res != 79083
        assert res == 29895
