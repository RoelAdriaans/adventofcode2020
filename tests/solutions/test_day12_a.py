import pytest

from adventofcode2020.solutions.day12 import Day12PartA, Direction


class TestDay12PartA:
    def test_day12a_next(self):
        south = Direction.SOUTH
        # Set the next direction
        west = Direction.get_next(south, 1)
        assert west == Direction.WEST

        east = Direction.get_next(west, -2)
        assert east == Direction.EAST

        # Test looping:
        assert Direction.get_next(Direction.NORTH, -2) == Direction.SOUTH

        assert Direction.get_next(west, 1) == Direction.NORTH

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [(["F10", "N3", "F7", "R90", "F11"], 25)]
    )
    def test_day12a_solve(self, input_data, expected_result):
        input_str = "\n".join(input_data)
        solution = Day12PartA()
        result = solution.solve(input_str)
        assert result == expected_result

    def test_day12a_data(self):
        """ Result we got when we did the real solution """
        solution = Day12PartA()
        res = solution("day_12/day12.txt")
        assert res != 746  # Too high
        assert res == 362
