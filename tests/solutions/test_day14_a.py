import pytest

from adventofcode2020.solutions.day14 import Day14PartA


class TestDay14PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                [
                    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
                    "mem[8] = 11",
                    "mem[7] = 101",
                    "mem[8] = 0",
                ],
                165,
            ),
        ],
    )
    def test_day14a_solve(self, input_data, expected_result):
        input_data = "\n".join(input_data)
        solution = Day14PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day14a_data(self):
        """ Result we got when we did the real solution """
        solution = Day14PartA()
        res = solution("day_14/day14.txt")
        assert res == 18630548206046
