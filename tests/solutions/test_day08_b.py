import pytest

from adventofcode2020.solutions.day08 import Day08PartB


class TestDay08PartB:
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

    @pytest.mark.parametrize(("input_data", "expected_result"), [(instruction_1, 8)])
    def test_day08b_solve(self, input_data, expected_result):
        solution = Day08PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day08b_data(self):
        """ Result we got when we did the real solution """
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        assert res == 2477
