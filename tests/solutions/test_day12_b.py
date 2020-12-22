import pytest

from adventofcode2020.solutions.day12 import Day12PartB, Location


class TestDay12PartB:
    @pytest.mark.parametrize(
        ("instructions", "expected_waypoint_loction"),
        [
            (["F10"], Location(horiz=10, vert=1)),  # Start point
            #
            (["F10", "R90"], Location(horiz=10, vert=-1)),  # One rotatation
            #
            (["F10", "R90", "R90"], Location(horiz=-10, vert=-1)),  # Two rotations
            (["F10", "R180"], Location(horiz=-10, vert=-1)),  # Two rotations
            #
            (["F10", "R90", "R90", "R90"], Location(horiz=-10, vert=1)),  # Three rot.
            #
            (["F10", "R180", "R180"], Location(horiz=10, vert=1)),  # Four rot.
            (["F10", "R360"], Location(horiz=10, vert=1)),  # Four rotations
            # And, to the left!
            (["F10", "L360"], Location(horiz=10, vert=1)),  # Four rotations
            (["F10", "L90"], Location(horiz=-10, vert=1)),  # One rotatation
            #
            (["F10", "L90", "L90"], Location(horiz=-10, vert=-1)),  # Two rotatation
            (["F10", "L180"], Location(horiz=-10, vert=-1)),  # Two rotatation
            #
            (["F10", "L90", "L90", "L90"], Location(horiz=10, vert=-1)),  # Three
            (["F10", "L180", "L90"], Location(horiz=10, vert=-1)),  # Three
        ],
    )
    def test_day12b_rotation(self, instructions, expected_waypoint_loction):
        input_str = "\n".join(instructions)
        solution = Day12PartB()
        # Run the solve, but we do not care about the result
        solution.solve(input_str)
        assert expected_waypoint_loction == solution.waypoint.location

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
        assert res == 0
