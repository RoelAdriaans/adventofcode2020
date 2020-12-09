import pytest

from adventofcode2020.solutions.day09 import Day09PartA


class TestDay09PartA:
    @pytest.mark.parametrize(("begin", "is_valid"), [(0, True), (1, True), (9, False)])
    def test_day09a_solve(self, begin, is_valid):
        """
        127 is false, and on place 14. That will mean that 9, 10, 11, 12, 13 is the
        preamble, 14 check digit. So we begin at 9
        """
        # fmt: off
        integers = [
            35, 20, 15, 25, 47, 40, 62, 55,
            65, 95, 102, 117, 150, 182, 127,
            219, 299, 277, 309, 576
        ]
        # fmt: on

        solution = Day09PartA()
        end = begin + 5
        slice = integers[begin:end]
        assert len(slice) == 5
        check_digit = integers[begin + 5]

        result = solution.check_preamble(integers=slice, next_number=check_digit)

        assert result is is_valid

    def test_day09a_data(self):
        """ Result we got when we did the real solution """
        solution = Day09PartA()
        res = solution("day_09/day09.txt")
        assert res != 53
        assert res == 1492208709
