import pytest

from adventofcode2020.solutions.day08 import Day08PartA


class TestDay08PartA:
    instruction_1 = "\n".join(
        [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]
    )

    @pytest.mark.parametrize(("instructions", "expected_result"), [(instruction_1, 5)])
    def test_day08a_solve(self, instructions, expected_result):
        solution = Day08PartA()
        result = solution.solve(instructions)
        assert result == expected_result

    def test_day08a_data(self):
        """ Result we got when we did the real solution """
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 2080
