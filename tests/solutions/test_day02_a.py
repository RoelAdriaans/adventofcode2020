import pytest

from adventofcode2020.solutions.day02 import Day02PartA, PassPol


class TestDay02PartA:
    def test_day02_split(self):
        input_str = "7-9 r: rrrkrrrrrnrrmj"

        result = Day02PartA.split(input_str)
        assert result == PassPol(
            at_least=7, at_most=9, letter="r", password="rrrkrrrrrnrrmj"
        )

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc\n", 2)],
    )
    def test_day02a_solve(self, input_data, expected_result):
        solution = Day02PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day02a_data(self):
        """ Result we got when we did the real solution """
        solution = Day02PartA()
        res = solution("day_02/day02.txt")
        assert res == 465
